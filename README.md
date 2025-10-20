# Nome do projeto:
Monitoramento de impressoras

# Descrição:
1. Simula e Automatiza uma Tarefa de TI
O script automatiza a tarefa repetitiva de verificar o status de múltiplas impressoras, ele lê uma lista de impressoras de um arquivo de texto (.txt) e, para cada uma, simula uma verificação,
atribuindo aleatoriamente um dos três status possíveis
A) Disponível: A impressora está online e pronta
B) Em Uso: A impressora está processando um trabalho
C) Travada: A fila de impressão tem um problema e precisa de intervenção (o script simula o cancelamento dos trabalhos).

2. Fornece um Painel de Controle Visual (Dashboard)
Através da interface gráfica (criada com Tkinter em Python ou Windows Forms em PowerShell), o script oferece um "dashboard" em tempo real.
O que se pode ver
A) Uma lista de todas as impressoras sendo monitoradas
B) O status atual de cada uma, destacado por cores (verde para disponível, amarelo para em uso, vermelho para travada)
C) Informações adicionais como o nome da fila e o setor ao qual a impressora pertence.

3. Registra Atividades para Auditoria e Diagnóstico (Log)
Tudo o que o script faz é registrado no arquivo log_monitoramento.txt com data e hora, isso é fundamental em um ambiente real de TI para
A) Saber quando uma verificação foi iniciada
B) Verificar o status de uma impressora em um horário específico
C) Diagnosticar erros no próprio script ou no processo.

4. Gerar Relatórios Estruturados (Report)
Com um clique no botão "Gerar Relatório", o script cria um arquivo relatorio.csv. Este arquivo é um "retrato" do estado de todas as impressoras no momento da última verificação. Por ser um arquivo CSV, ele pode ser facilmente aberto no Excel para
A) Analisar dados (ex: qual setor tem mais impressoras travadas?)
B) Manter um histórico de status
C) Enviar um resumo para a gestão

Essa é uma ferramenta ideal para
A) Analistas de Suporte e Help Desk: Para automatizar uma verificação de rotina e rapidamente identificar problemas
B) Administradores de Sistemas: Para ter uma visão centralizada do parque de impressão
C) Estudantes e Desenvolvedores: Como um excelente projeto prático para aprender sobre automação, manipulação de arquivos, criação de interfaces gráficas e lógica de programação em Python e PowerShell.

O objetivo é transformar um processo manual e reativo de "checar impressoras uma por uma" em um processo proativo, automatizado e centralizado, economizando tempo e permitindo uma resposta mais rápida a problemas.

# Como instalar
Para o script em Python (.py)
O Python é uma linguagem que precisa ser instalada no seu computador.
A biblioteca para a interface gráfica (Tkinter) geralmente já vem incluída na instalação padrão no Windows.

Passo 1: Instalar o Python
Se você ainda não tem o Python instalado, baixe-o do site oficial: https://www.python.org/downloads/
Execute o instalador.
* MUITO IMPORTANTE: Na primeira tela da instalação, marque a caixa que diz "Add Python to PATH" ou "Adicionar Python ao PATH".
Isso simplificará muito a execução do script.
Prossiga com a instalação padrão.

Passo 2: Preparar a Pasta e os Arquivos
Crie a seguinte estrutura de pastas no seu computador.
O caminho precisa ser exatamente este, pois está definido no script:
D:\Meus projetos\Monitoramento de impressao 2025
Dentro desta pasta, crie um arquivo de texto chamado impressoras.txt.
Abra o impressoras.txt com o Bloco de Notas e coloque o conteúdo com o cabeçalho e as suas impressoras, exatamente como no exemplo abaixo (usando ; como separador):
EX:
impressora;status;fila;setor
HP_PRODUCAO_01;Disponivel;FILA_PROD_01;Produção
EPSON_FINANC_05;Em Manutencao;FILA_FIN_05;Financeiro
BROTHER_RH_02;Disponivel;FILA_RH_02;Recursos Humanos
Salve o arquivo com a codificação UTF-8 para garantir que os caracteres especiais (como ç e ã) funcionem.
No Bloco de Notas, ao clicar em "Salvar como", você pode escolher a codificação na parte de baixo da janela.

Passo 3: Salvar e Executar o Script
Copie o código Python que eu forneci.
Cole-o em um novo arquivo de texto e salve-o como monitor_impressoras.py dentro da pasta D:\Meus projetos\Monitoramento de impressao 2025.
Para executar: Abra o "Prompt de Comando" ou "PowerShell" do Windows.
Navegue até a pasta do projeto digitando o comando e pressionando Enter: cd "D:\Meus projetos\Monitoramento de impressao 2025"
Execute o script com o comando: python monitor_impressoras.py
A janela do programa deverá aparecer.

2: Para o script em PowerShell (.ps1)
O PowerShell já vem instalado por padrão no Windows 10 e 11, então você não precisa instalar nada.
Passo 1: Preparar a Pasta e os Arquivos
Crie a seguinte estrutura de pastas (se ainda não tiver criado): D:\Meus projetos\Monitoramento de impressao 2025
Crie o arquivo impressoras.txt dentro desta pasta, com o mesmo conteúdo e formato (separado por ; e salvo como UTF-8) do exemplo da seção Python.

Passo 2: Salvar e Executar o Script
Copie o código PowerShell que eu forneci.
Cole-o em um novo arquivo de texto e salve-o como monitor_impressoras.ps1 dentro da pasta D:\Meus projetos\Monitoramento de impressao 2025.

Passo 3: Executar o Script
Abra o "PowerShell" (procure por ele no Menu Iniciar).
Navegue até a pasta do projeto com o comando: cd "D:\Meus projetos\Monitoramento de impressao 2025"
Tente executar o script com o comando: .\monitor_impressoras.ps1
Se Ocorrer um Erro de Execução (Muito Comum)
Por padrão, o PowerShell bloqueia a execução de scripts por segurança. Se você vir um erro em vermelho falando sobre "a execução de scripts foi desabilitada neste sistema", você precisa liberar a permissão apenas para esta sessão.
No mesmo terminal PowerShell, digite o seguinte comando e pressione Enter:
PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Ele pode pedir uma confirmação, digite S (para Sim) e pressione Enter.
Agora, tente executar o script novamente: .\monitor_impressoras.ps1
A janela do programa deverá aparecer.

# Funcionalidades:
1. O script não possui uma lista fixa de impressoras em seu código
*  O que faz: Ele lê o arquivo impressoras.txt toda vez que o monitoramento é iniciado
*  Como funciona: Você define quais impressoras serão monitoradas simplesmente editando este arquivo de texto, cada linha representa uma impressora com seus dados separados por ponto e vírgula (;)
*  Benefício: Flexibilidade total, qualquer pessoa pode adicionar, remover ou alterar impressoras sem precisar modificar o código-fonte do programa.

2. Simulação de Monitoramento Ativo
Esta é a função central do script, ativada pelo botão "Iniciar Monitoramento"
* O que faz: Percorre a lista de impressoras do arquivo .txt e atribui a cada uma um status aleatório para simular uma verificação real
* Como funciona: Para cada impressora, o script sorteia um de três status ('Disponível', 'Em Uso' ou 'Travada') e simula uma ação correspondente (verifica serviço, identifica em uso, cancela trabalhos travados)
* Benefício: Cria um ambiente dinâmico e realista para demonstrar ou testar o processo de monitoramento sem qualquer risco a um sistema de produção.

3. Interface Gráfica e Visualização em Tempo Real
O script apresenta os dados em uma janela gráfica, agindo como um painel de controle
* O que faz: Exibe a lista de impressoras e seus status de forma clara e organizada
* Como funciona: A tabela na janela é atualizada impressora por impressora durante a simulação, ela usa um sistema de cores intuitivo para indicar o status
A) Verde: Disponível
B) Amarelo: Em uso
C) Vermelho: Travada
* Benefício: Permite a identificação visual e imediata de problemas, tornando a análise muito mais rápida do que ler logs ou saídas de texto em um console.

4. Geração de Log Detalhado
O script mantém um registro cronológico de todas as suas ações
* O que faz: Cria e atualiza o arquivo log_monitoramento.txt.
* Como funciona: Cada ação importante — inicia o programa, começa uma verificação, o status encontrado para cada impressora, gera um relatório,
  encontra um erro e salva no log com a data e hora exatas (dd-MM-yyyy HH:mm:ss)
* Benefício: Fornece um histórico completo para auditoria, rastreamento de eventos e diagnóstico de falhas, se algo der errado, o log é o primeiro lugar a se olhar.

5. Exportação de Relatórios Estruturados (CSV)
Ativado pelo botão "Gerar Relatório", esta função serve para consolidar os dados
* O que faz: Pega o resultado da última simulação de monitoramento e o salva no arquivo relatorio.csv
* Como funciona: O arquivo CSV é formatado como uma planilha, com colunas bem definidas (impressora, status, fila, setor, etc.), podendo ser aberto diretamente no Excel ou em outras ferramentas de análise
* Benefício: Transforma os dados voláteis da simulação em um registro permanente e fácil de analisar, compartilhar ou arquivar.

# Desenvolvimento e Depuração:
1. O Processo de Desenvolvimento (Development) seguiu as seguintes etapas:
Etapa A: Definição dos Requisitos
Foi definido o que o script precisava fazer:
A) Ler uma lista de impressoras de um arquivo
B) Ter uma interface gráfica com botões
C) Simular três status: disponível, em uso e travada
D) Realizar ações simuladas com base no status
E) Gerar um log em tempo real
F) Criar um relatório final em CSV

Etapa B: Escolha da Tecnologia e Arquitetura
Com os requisitos definidos, foi escolhido as seguintes ferramentas
A) Linguagens: Python e PowerShell, para atender as duas opções de linguagens
B) Interface Gráfica (GUI): Tkinter para Python (padrão e fácil de usar) e Windows Forms para PowerShell (nativo do Windows)
C) Estrutura do Código: Foi decidido separar a lógica em funções claras e reutilizáveis (logar_mensagem, simular_monitoramento, gerar_relatorio), isso torna o código mais organizado e fácil de manter

Etapa C: Codificação (Escrever o Código)
Esta foi a fase de traduzir a arquitetura e os requisitos em código. Foi escrito as funções, criado a janela, os botões e a tabela e implementamos a lógica de simulação com status aleatórios.

Etapa D: Refinamento Iterativo
O desenvolvimento raramente é um processo linear, foi feito de forma iterativa
A) Criado uma versão funcional
B) verifica se o arquivo existe, tornando-o mais robusto, lendo o arquivo impressoras.txt
C) o desenvolvimento foi o ato de construir o "motor" e o "chassi" do programa

2. O Processo de Depuração (Debugging)
O script passou por dois ciclos de depuração claros durante a interação
1: O Cabeçalho do Arquivo Aparecia no Log
* O Bug (Sintoma): Foi notado que a primeira linha do arquivo (impressora;status;fila;setor) estava sendo tratada como uma impressora real
A) A Investigação (Análise)
B) Hipótese: O código não estava pulando a primeira linha do arquivo
C) Verificação: Analisado as funções csv.DictReader (Python) e Import-Csv (PowerShell), ambas são projetadas para usar a primeira linha como cabeçalho automaticamente, a lógica estava correta
Conclusão: O problema não era um "bug" no código, mas uma potencial má interpretação ou um formato de arquivo inesperado.
* A Correção (Solução): Foi reforçado no código o tratamento de erros para o caso de o cabeçalho estar errado, foi ajustado a lógica para ser mais clara sobre como o arquivo deveria ser.

2: O Relatório CSV Não Era Gerado
O Bug (Sintoma): O arquivo relatorio.csv não aparecia após clicar no botão
A) A Investigação (Análise)
B) Hipóteses: O programa não tinha permissão para escrever o arquivo na pasta, O monitoramento falhou e então não havia dados para gerar o relatório e ocorreu um erro silencioso durante a gravação
C) Plano de Ação: Foi criado um guia de depuração: verificar a ordem dos cliques, olhar o arquivo de log por mensagens de ERRO e tentar executar como administrador
* A Correção (Solução): foi adicionado mais mensagens de log (logar_mensagem) na função gerar_relatorio, isso é uma técnica de depuração clássica: aumentar a "visibilidade" do que o programa está fazendo, com os novos logs, se o erro ocorrer novamente, poderemos saber exatamente em que ponto o processo falhou.

# Ferramentas e Boas Práticas
1. Para Desenvolvimento
A) IDEs (Ambientes de Desenvolvimento): Ferramentas como VS Code, PyCharm ou o PowerShell ISE ajudam a escrever código mais rápido e com menos erros
* Comentários: Escrever comentários no código (# Exemplo de comentário) para explicar partes complexas é crucial para a manutenção futura.

2. Para Depuração
A) Logs: um bom sistema de logs é a ferramenta de depuração mais importante
B) Comandos print / Write-Host: A forma mais simples de depurar é inserir comandos para imprimir o valor de uma variável em um ponto específico e ver se está correto
C) Debuggers: Ferramentas avançadas (presentes em IDEs) que permitem pausar a execução do código em uma linha específica (breakpoint), inspecionar todas as variáveis e avançar linha por linha para encontrar o ponto exato do erro

# # Tecnologias usadas:
Linguagem Python e PowerShell
