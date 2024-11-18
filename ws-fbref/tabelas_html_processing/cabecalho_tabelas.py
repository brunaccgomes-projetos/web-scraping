from bs4 import BeautifulSoup
import pandas as pd

def processar_cabecalho_html(html_content):
    """
    Processa o cabeçalho de uma tabela HTML e retorna uma lista de nomes de colunas para o CSV.
    """

    # Parseia o conteúdo HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')

    if not table:
        raise ValueError("O HTML não contém uma tabela.")

    # Verifica se existe a tag <thead> e, dentro dela, pelo menos uma tag <tr>
    thead = table.find('thead')
    if not thead:
        raise ValueError("A tabela não contém a tag <thead>.")
     
    rows = thead.find_all('tr')
    if len(rows) < 2:
        raise ValueError("A tag <thead> da tabela deve conter pelo menos duas linhas (<tr>).")

    # Extrai as células (th) das duas primeiras linhas
    primeira_linha = rows[0].find_all('th')
    segunda_linha = rows[1].find_all('th')

    if not primeira_linha or not segunda_linha:
        raise ValueError("As duas primeiras linhas do cabeçalho não contêm células (<th>).")

    # Cria prefixos para colunas com `colspan` na primeira linha
    prefixos = []
    for th in primeira_linha:
        colspan = int(th.get('colspan', 1))
        texto = th.get_text(strip=True)
        prefixo = texto[:3] + "_" if texto else ""
        prefixos.extend([prefixo] * colspan)

    # Define os cabeçalhos para a segunda linha com ou sem prefixo
    cabecalho = []
    for i, th in enumerate(segunda_linha):
        texto_coluna = th.get_text(strip=True)
        coluna_nome = prefixos[i] + texto_coluna if prefixos[i] else texto_coluna
        cabecalho.append(coluna_nome)


    return cabecalho

def salvar_csv_com_cabecalho(html_content, arquivo_csv):
    """
    Processa o HTML e salva a tabela em um CSV com o cabeçalho modificado.
    """
    # Parseia o conteúdo HTML e cria o cabeçalho
    cabecalho = processar_cabecalho_html(html_content)
    
    # Extrai dados da tabela usando pandas e salva com o cabeçalho personalizado
    df = pd.read_html(html_content, header=1)[0]  # Lê a tabela a partir da segunda linha
    df.columns = cabecalho  # Define o cabeçalho personalizado
    df.to_csv(arquivo_csv, index=False)  # Salva em CSV

    print(f"Tabela salva com sucesso em {arquivo_csv}")

# Exemplo de uso:
if __name__ == "__main__":
    with open('caminho_para_seu_arquivo.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    salvar_csv_com_cabecalho(html_content, 'saida_tabela.csv')
