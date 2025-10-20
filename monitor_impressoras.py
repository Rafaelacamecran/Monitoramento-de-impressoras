import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import random
from datetime import datetime
import time

# --- CONFIGURAÇÃO ---
DIRETORIO_PROJETO = r"D:\Meus projetos\Monitoramento de impressao 2025"
ARQUIVO_IMPRESSORAS = os.path.join(DIRETORIO_PROJETO, "impressoras.txt")
ARQUIVO_RELATORIO = os.path.join(DIRETORIO_PROJETO, "relatorio.csv")
ARQUIVO_LOG = os.path.join(DIRETORIO_PROJETO, "log_monitoramento.txt")

dados_atuais_impressoras = []

# --- FUNÇÕES ---

def logar_mensagem(mensagem):
    """Escreve uma mensagem com timestamp no arquivo de log."""
    agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_entry = f"[{agora}] - {mensagem}\n"
    print(log_entry.strip())
    with open(ARQUIVO_LOG, 'a', encoding='utf-8') as f:
        f.write(log_entry)

def simular_monitoramento():
    """Função principal que simula o monitoramento das impressoras."""
    global dados_atuais_impressoras
    dados_atuais_impressoras.clear()
    
    for item in tree.get_children():
        tree.delete(item)

    # Verifica se o arquivo .txt existe antes de continuar
    if not os.path.exists(ARQUIVO_IMPRESSORAS):
        msg_erro = f"Arquivo de impressoras não encontrado!\n\nCrie o arquivo em:\n{ARQUIVO_IMPRESSORAS}\n\nE certifique-se que ele tenha o cabeçalho 'impressora;status;fila;setor'."
        logar_mensagem(f"ERRO: {msg_erro}")
        messagebox.showerror("Arquivo não encontrado", msg_erro)
        return

    logar_mensagem("--- INICIANDO NOVA VERIFICAÇÃO ---")
    
    try:
        # A leitura funciona da mesma forma para .txt, desde que o conteúdo seja delimitado
        with open(ARQUIVO_IMPRESSORAS, 'r', encoding='utf-8-sig') as f:
            leitor_csv = csv.DictReader(f, delimiter=';')
            
            for linha in leitor_csv:
                impressora = linha['impressora']
                status = linha['status']
                fila = linha['fila']
                setor = linha['setor']
                
                status_possiveis = ['disponível', 'em uso', 'travada']
                status_simulado = random.choice(status_possiveis)
                
                logar_mensagem(f"Verificando {impressora} no setor {setor} no status {status}...")
                
                if status_simulado == 'disponível':
                    acao = "Serviço verificado"
                    logar_mensagem(f"  -> Status: Disponível. Fila '{fila}' está OK.")
                elif status_simulado == 'em uso':
                    acao = "Em operação"
                    logar_mensagem(f"  -> Status: Em Uso. Fila '{fila}' está processando trabalhos.")
                elif status_simulado == 'travada':
                    acao = "Trabalhos cancelados"
                    logar_mensagem(f"  -> Status: Travada! Fila '{fila}' bloqueada. Simulando cancelamento.")

                tree.insert("", "end", values=(impressora, status_simulado.upper(), fila, setor), tags=(status_simulado,))
                
                dados_atuais_impressoras.append({
                    'impressora': impressora, 'status': status_simulado, 'fila': fila,
                    'setor': setor, 'acao_simulada': acao,
                    'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                })
                
                app.update()
                time.sleep(0.5)

    except KeyError as e:
        msg_erro = f"ERRO: O arquivo '{os.path.basename(ARQUIVO_IMPRESSORAS)}' não possui a coluna esperada: {e}. Verifique se o cabeçalho (primeira linha) está correto."
        logar_mensagem(msg_erro)
        messagebox.showerror("Erro de Formato", msg_erro)
    except Exception as e:
        logar_mensagem(f"ERRO ao ler o arquivo de impressoras: {e}")
        messagebox.showerror("Erro de Leitura", f"Ocorreu um erro ao processar o arquivo: {e}")
    
    logar_mensagem("--- VERIFICAÇÃO CONCLUÍDA ---")
    messagebox.showinfo("Concluído", "Monitoramento simulado com sucesso!")

def gerar_relatorio():
    """Gera um arquivo CSV com o último status verificado."""
    if not dados_atuais_impressoras:
        messagebox.showwarning("Aviso", "Nenhum dado para gerar relatório. Por favor, inicie o monitoramento primeiro.")
        return
        
    try:
        with open(ARQUIVO_RELATORIO, 'w', newline='', encoding='utf-8-sig') as f:
            campos = ['impressora', 'status', 'fila', 'setor', 'acao_simulada', 'timestamp']
            escritor = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            escritor.writeheader()
            escritor.writerows(dados_atuais_impressoras)
        
        logar_mensagem(f"Relatório gerado com sucesso em: {ARQUIVO_RELATORIO}")
        messagebox.showinfo("Sucesso", f"Relatório salvo em:\n{ARQUIVO_RELATORIO}")
    except Exception as e:
        logar_mensagem(f"ERRO ao gerar relatório: {e}")
        messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar o relatório: {e}")

# --- INTERFACE GRÁFICA ---

app = tk.Tk()
app.title("Simulador de Monitoramento de Impressoras")
app.geometry("800x500")

frame = ttk.Frame(app, padding="10")
frame.pack(fill=tk.BOTH, expand=True)
frame_botoes = ttk.Frame(frame)
frame_botoes.pack(fill=tk.X, pady=5)
btn_monitorar = ttk.Button(frame_botoes, text="Iniciar Monitoramento", command=simular_monitoramento)
btn_monitorar.pack(side=tk.LEFT, padx=5)
btn_relatorio = ttk.Button(frame_botoes, text="Gerar Relatório", command=gerar_relatorio)
btn_relatorio.pack(side=tk.LEFT, padx=5)
btn_sair = ttk.Button(frame_botoes, text="Sair", command=app.quit)
btn_sair.pack(side=tk.RIGHT, padx=5)

cols = ('Impressora', 'Status', 'Fila', 'Setor')
tree = ttk.Treeview(frame, columns=cols, show='headings', height=15)
for col in cols:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True, pady=10)

tree.tag_configure('disponível', background='pale green')
tree.tag_configure('em uso', background='light yellow')
tree.tag_configure('travada', background='salmon')

# --- INICIALIZAÇÃO ---
if not os.path.exists(DIRETORIO_PROJETO):
    os.makedirs(DIRETORIO_PROJETO)
logar_mensagem("Aplicação iniciada. Lendo de 'impressoras.txt'.")

app.mainloop()