## 1. Criar o Ambiente Virtual

**1.1. Abra o terminal ou o PowerShell no Windows.**

**1.2. Navegue até o diretório base do projeto:**
cd D:\GitHub\web-scraping\ws-fbref

**1.3. Crie o ambiente virtual:**
python -m venv venv

**1.4. Ative o ambiente virtual:**
venv\Scripts\activate

## 2. Instalar as Dependências

**Instale as dependências necessárias com pip, se ainda não tiver feito isso (caso contrário, pule esta etapa):**
pip install pandas beautifulsoup4 lxml selenium webdriver-manager

## 3. Gerar o Arquivo requirements.txt

**O arquivo requirements.txt define todas as bibliotecas necessárias para rodar o script.**
pip freeze > requirements.txt

**Ou instale as dependências do arquivo requirements.txt existente**
pip install -r requirements.txt

## 4. Executar o Script

**4.1. Navegue até o diretório onde está o script:**
cd D:\GitHub\web-scraping\ws-fbref

**4.2. Execute o script com o Python:**
python ws_fbref_jogador.py

## 5. Manutenção do Ambiente

**5.1. Para Desativar o Ambiente:**
**Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:**
deactivate

**5.2. Para Reativar o Ambiente:**
**Sempre que quiser executar novamente, reative o ambiente com:**
venv\Scripts\activate
