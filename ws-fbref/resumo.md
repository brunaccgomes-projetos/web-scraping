## Resumo:

Os dados extraídos estão disponíveis na plataforma FBREF ([fbref.com](https://fbref.com/pt)).

Esta aplicação realiza extração de dados de jogadores disponíveis por código do jogador na plataforma, por ano e por competições (sendo possível extrair de todas as competições), iniciando no tópico "Resumo" através do link de Históricos de Jogos: https://fbref.com/pt/jogadores/{jogador['codigo']}/partidas/{year}/{tipo_url}

**Arquivo de configuração:** jogadores_config.json

O Histórico de Jogos de cada jogador está dividido por tópicos, identificado no arquivo de configuração, contendo texto título e palavra chave da url.

- "tipos_registro" ({tipo_url} em ws_fbref_jogador.py)
  -"Resumo": "summary";
  -"Passes": "passing";
  -"Tipos de Passes": "passing_types";
  -"Gols e Criação de Chutes": "gca";
  -"Ações Defensivas": "defense";
  -"Posse": "possession";
  -"Estatísticas Variadas": "misc".

Os dados dos jogadores são utilizados para indicar a realização de scraping, gerar url dos dados de extração e criação dos diretórios de arquivos csv que serão carregados com os dados. São informados para os seguintes atributos:

- "jogadores": [
  {
  "nome": "nomedojogador",
  "codigo": "be8d02dd",
  "st_process": 1
  },...
  ]

**Arquivo de Log:** registra execução da aplicação

Insere arquivos de log no diretório ws-fbref\log_ws sob fluxo e formato:

- 1. Inserir as seguintes linhas:
  - "Início da Execução..."
  - "------------"
  - dt_hr_ini_log: data e hora inicial (yyyy-mm-dd hh:mm:ss) da execução do script;
  - nm_tarefa: nome do processo executado(aqui no caso o valor sempre será extr_ws);
  - nm_ide: nome e versão do browser do processo executado;
  - nm_arquivo_exec: nome do arquivo que contém o script executado.
- 2. A cada iteração de {ano} com {tipo de registro}, insere os registros (linhas) contendo os seguintes atributos separados por "|",:
  - dt_hr_ini: data e hora (yyyy-mm-dd hh:mm:ss) do início da execução da iteração;
  - st_exec: ok ou falha (True ou False) para sucesso da execução da iteração;
  - st_arquivo: sim ou não (True ou False) para indicar se o arquivo de dados foi gerado ou não;
  - nm*dados: {ano}*{tipo de registro}.csv para nome do arquivo gerado com os dados extraídos da iteração;
  - erro: caso falha na execução da iteração, gerar arquivo contendo a mensagem de erro completa, salvar o arquivo dentro da mesma pasta de log com nome erro*log*{hhmmss}_{ano}_{tipo de registro}.txt e gravar este nome do arquivo nessa coluna;
  - dt_hr_fim: data e hora (yyyy-mm-dd hh:mm:ss) do fim da execução da iteração;
- 3. Inserir as seguintes linhas:
  - "------------"
  - "Fim da Execução..."
