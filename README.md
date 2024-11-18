# Web Scraping Projects

Este repositório contém projetos de web scraping desenvolvidos em Python, com foco em extração automatizada de dados estruturados a partir de fontes online. Cada projeto está organizado em pastas separadas, com scripts e recursos necessários para realizar as tarefas de extração, tratamento e armazenamento dos dados.

---

## 📁 Estrutura do Repositório

- **ws-fbref/**: Projeto de web scraping que implementa a extração de tabelas HTML de uma fonte específica, salvando os dados em formato CSV com logs detalhados do processo.

Outros projetos serão adicionados em breve.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

Os projetos deste repositório utilizam as seguintes ferramentas e bibliotecas:

- **Linguagem**: Python (3.12+)
- **Bibliotecas**:
  - `selenium` (para navegação e extração dinâmica de dados)
  - `pandas` (para manipulação e armazenamento de dados em tabelas)
  - `beautifulsoup4` (para parsing HTML)
  - `lxml` (para suporte avançado a HTML e XML)
  - `chromedriver-autoinstaller` (para instalação automática do ChromeDriver)
- **Ambiente Virtual**: Configurado com `venv`.

---

## 📝 Recursos Gerais

Cada projeto inclui:

1. **Scripts principais**:
   - Automação do processo de navegação e extração de dados.
   - Configuração flexível para diferentes fontes de dados.
   - Suporte para diferentes tipos de conteúdo (tabelas, listas, etc.).

2. **Logs detalhados**:
   - Registro de cada etapa do processo, incluindo status de execução e possíveis erros.
   - Arquivos de log salvos automaticamente para auditoria e análise.

3. **Dados extraídos**:
   - Armazenamento dos dados em formato CSV ou outros formatos conforme o projeto.
   - Organização dos arquivos por estrutura lógica, como diretórios baseados no tipo de dado ou período.

4. **Reutilização**:
   - Estrutura flexível que permite a customização para diferentes cenários de scraping.
   - Componentes modulares para adaptar scripts a novas fontes de dados.

---

## 🚀 Como Executar um Projeto

### Passos Gerais

1. Clone o repositório:
   ```bash
   git clone https://github.com/brunaccgomes-projetos/web-scraping.git
   cd web-scraping
