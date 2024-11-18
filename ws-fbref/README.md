## Descrição:

Esta aplicação realiza extração de dados de jogadores disponíveis na plataforma FBREF ([fbref.com](https://fbref.com/pt)) via **web scraping**.
A url de extração inicial é referente ao Históricos de Jogos iniciando no tópico "Resumo" através da url https://fbref.com/pt/jogadores/{jogador['codigo']}/partidas/{year}/{tipo_url}, substituindo:

- **{jogador['codigo']}:** o código do jogador na plataforma;
- **{ano}:** ano de referência;
- **{tipo_url}:** "tipos_registro"
  - _"Resumo":_ "summary";
  - _"Passes":_ "passing";
  - _"Tipos de Passes":_ "passing_types";
  - _"Gols e Criação de Chutes":_ "gca";
  - _"Ações Defensivas":_ "defense";
  - _"Posse":_ "possession";
  - _"Estatísticas Variadas":_ "misc".

## Arquivo de configuração:

_jogadores_config.json_

Os dados dos jogadores são utilizados para indicar a realização de scraping, gerar url dos dados de extração e criação dos diretórios de arquivos csv que serão carregados com os dados. São informados para os seguintes atributos:

- **"jogadores":**
  - _"nome":_ "nomedojogador",
  - _"codigo":_ "be8d02dd",
  - _"st_process":_ 1

## Arquivo de Log:

_registra execução da aplicação_

Insere arquivos de log no diretório _ws-fbref\log_ws_ sob fluxo e formato:

- **1. Inserir as seguintes linhas:**
  - _"Início da Execução..."_
  - _"------------"_
  - _dt_hr_ini_log:_ data e hora inicial (yyyy-mm-dd hh:mm:ss) da execução do script;
  - _nm_tarefa:_ nome do processo executado(aqui no caso o valor sempre será extr_ws);
  - _nm_ide:_ nome e versão do browser do processo executado;
  - _nm_arquivo_exec:_ nome do arquivo que contém o script executado.
- **2. A cada iteração de {ano} com {tipo de registro}, insere os registros (linhas) contendo os seguintes atributos separados por "|",:**
  - _dt_hr_ini:_ data e hora (yyyy-mm-dd hh:mm:ss) do início da execução da iteração;
  - _st_exec:_ ok ou falha (True ou False) para sucesso da execução da iteração;
  - _st_arquivo:_ sim ou não (True ou False) para indicar se o arquivo de dados foi gerado ou não;
  - _nmdados:_ {ano}\*{tipo de registro}.csv para nome do arquivo gerado com os dados extraídos da iteração;
  - _erro:_ caso falha na execução da iteração, gerar arquivo contendo a mensagem de erro completa, salvar o arquivo dentro da mesma pasta de log com nome _erro*log*{hhmmss}*{ano}*{tipo de registro}.txt_ e gravar este nome do arquivo nessa coluna;
  - _dt_hr_fim:_ data e hora (yyyy-mm-dd hh:mm:ss) do fim da execução da iteração;
- **3. Inserir as seguintes linhas:**
  - _"------------"_
  - _"Fim da Execução..."_

## Especificação Técnica

- **IDE:** VSCode (Visual Studio Code)
- **Linguagem:** Python
  - **Bibliotecas (principais):** pandas, selenium, ChromeDriverManager, logging..

## Configuração e Execução

### 1. Criar o Ambiente Virtual

- **1.1. Abra o terminal ou o PowerShell no Windows.**

- **1.2. Navegue até o diretório base do projeto:**
  cd D:\GitHub\web-scraping\ws-fbref

- **1.3. Crie o ambiente virtual:**
  python -m venv venv

- **1.4. Ative o ambiente virtual:**
  venv\Scripts\activate

### 2. Instalar as Dependências

- **2.1. Instale as dependências do arquivo requirements.txt existente**
  pip install -r requirements.txt

- **2.2. OU CASO exclua o arquivo requirements.txt existente:**
  - **2.2.1. Primeiro: Instale as dependências necessárias com pip:**
    pip install pandas beautifulsoup4 lxml selenium webdriver-manager
  - **2.2.2. Segundo: Gere arquivo requirements.txt**
    pip freeze > requirements.txt

### 3. Executar o Script

- **3.1. Navegue até o diretório onde está o script:**
  cd D:\GitHub\web-scraping\ws-fbref

- **3.2. Execute o script com o Python:**
  python ws_fbref_jogador.py

### 4. Manutenção do Ambiente

- **4.1. Para Desativar o Ambiente:**
  **Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:**
  deactivate

- **4.2. Para Reativar o Ambiente:**
  **Sempre que quiser executar novamente, reative o ambiente com:**
  venv\Scripts\activate
