import os
import json
import time
import logging
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from tabelas_html_processing.cabecalho_tabelas import processar_cabecalho_html

# Caminho de configurações
config_file = "jogadores_config.json"
log_dir = "D:\\GitHub\\web-scraping\\ws-fbref\\log_ws"

# Função para carregar configurações
def load_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para inicializar o Logger
def init_log(log_file):
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write("dt_hr_ini;st_exec;st_arquivo;nm_dados;erro;dt_hr_fim\n")

# Função para registrar logs
def log_info(log_file, dt_hr_ini, st_exec, st_arquivo, nm_dados, erro, dt_hr_fim):
    with open(log_file, 'a', encoding='utf-8') as log:
        log.write(f"{dt_hr_ini};{st_exec};{st_arquivo};{nm_dados};{erro};{dt_hr_fim}\n")

# Função para salvar tabela em CSV
def save_table_to_csv(dataframe, filename, jogador_dir, year):
    year_dir = os.path.join(jogador_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)
    csv_path = os.path.join(year_dir, filename)
    dataframe.to_csv(csv_path, sep=";", index=False, encoding="utf-8")
    return csv_path

# Função para verificar se uma string é uma data válida no formato aaaa-mm-dd
def is_valid_date(date_str):
    try:
        pd.to_datetime(date_str, format='%Y-%m-%d')
        return True
    except ValueError:
        return False

def limpa_df(ndf):
    # Definindo o índice da coluna que queremos verificar (0 para a primeira coluna)
    indice_coluna = 0

    # Contando o número de linhas antes da exclusão
    num_linhas_inicial = ndf.shape[0]

    # Excluindo linhas onde a coluna especificada está vazia ou é null
    ndf = ndf[ndf.iloc[:, indice_coluna].notnull() & (ndf.iloc[:, indice_coluna] != '')].copy()
    # Excluindo linhas onde a coluna especificada possui texto "Data" ou não é uma data válida
    ndf = ndf[~(ndf.iloc[:, indice_coluna] == "Data") & ndf.iloc[:, indice_coluna].apply(is_valid_date)]

    # Contando o número de linhas após a exclusão
    num_linhas_final = ndf.shape[0]
    # Calculando o número de linhas excluídas
    num_linhas_excluidas = num_linhas_inicial - num_linhas_final
    # Exibindo o resultado
    print(f"Número de linhas excluídas: {num_linhas_excluidas}")
    
    return ndf

# Configurações do Webdriver
def configure_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Chrome/131.0.6778.70")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Carregar configurações
config = load_config(config_file)
anos = config['anos']
tipos_registro = config['tipos_registro']
jogadores = [j for j in config['jogadores'] if j['st_process'] == 1]

# Inicializar Webdriver
driver = configure_webdriver()

try:
    for jogador in jogadores:
        jogador_dir = f"D:\\GitHub\\web-scraping\\ws-fbref\\dados_ws\\{jogador['nome']}"
        log_file = os.path.join(log_dir, f"log_{jogador['nome']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv")
        init_log(log_file)

        for year in anos:
            for tipo, tipo_url in tipos_registro.items():
                dt_hr_ini = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                url = f"https://fbref.com/pt/jogadores/{jogador['codigo']}/partidas/{year}/{tipo_url}/"
                file_name = f"{year}_{tipo.replace(' ', '_').lower()}.csv"
                try:
                    driver.get(url)
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "matchlogs_all")))
                    table = driver.find_element(By.ID, "matchlogs_all")
                    table_html = table.get_attribute('outerHTML')
                    df = pd.read_html(table_html)[0]
                    df.columns = processar_cabecalho_html(table_html)
                    n_df = limpa_df(df)
                    save_table_to_csv(n_df, file_name, jogador_dir, year)
                    log_info(log_file, dt_hr_ini, "ok", "sim", file_name, "", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                except (TimeoutException, WebDriverException) as e:
                    error_file = f"erro_log_{datetime.now().strftime('%H%M%S')}_{year}_{tipo.replace(' ', '_').lower()}.txt"
                    with open(os.path.join(log_dir, error_file), 'w', encoding='utf-8') as f:
                        f.write(str(e))
                    log_info(log_file, dt_hr_ini, "falha", "não", file_name, error_file, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
except Exception as e:
    logging.error(f"Erro geral na execução: {e}")
finally:
    driver.quit()
