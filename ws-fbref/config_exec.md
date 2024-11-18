## Configuração e Execução

### 1. Criar o Ambiente Virtual

**1.1. Abra o terminal ou o PowerShell no Windows.**

**1.2. Navegue até o diretório base do projeto:**
cd D:\GitHub\web-scraping\ws-fbref

**1.3. Crie o ambiente virtual:**
python -m venv venv

**1.4. Ative o ambiente virtual:**
venv\Scripts\activate

### 2. Instalar as Dependências

**Instale as dependências do arquivo requirements.txt existente**
pip install -r requirements.txt

**OU CASO exclua o arquivo requirements.txt existente:**

- **Primeiro: Instale as dependências necessárias com pip:**
  pip install pandas beautifulsoup4 lxml selenium webdriver-manager
- **Segundo: Gere arquivo requirements.txt**
  pip freeze > requirements.txt

### 3. Executar o Script

**3.1. Navegue até o diretório onde está o script:**
cd D:\GitHub\web-scraping\ws-fbref

**3.2. Execute o script com o Python:**
python ws_fbref_jogador.py

### 4. Manutenção do Ambiente

**4.1. Para Desativar o Ambiente:**
**Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:**
deactivate

**4.2. Para Reativar o Ambiente:**
**Sempre que quiser executar novamente, reative o ambiente com:**
venv\Scripts\activate
