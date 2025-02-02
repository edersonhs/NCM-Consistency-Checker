import pandas as pd
from functions import otimizar_ncm_data, carregar_dados_ncms, grava_arquivo

# Carregar os dados da API
ncms_api = otimizar_ncm_data(
    carregar_dados_ncms('https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json'))

# Carregar a planilha
file_path = 'TabelaNCM2022.xlsx'

# Ler a coluna dos NCMs da planilha
df = pd.read_excel(file_path, sheet_name='NCM X uTrib_Vig 1-1-2025', dtype={'NCM': str}) # dtype={'NCM': str} para evitar que o pandas converta o NCM para inteiro
planilha = df['NCM'].str.replace('.', '').str.strip()

# Comparação de NCMs da planilha com a API
ncms_diferentes = []
ncms_iguais = []

for ncm_planilha in planilha:
    if ncm_planilha in ncms_api:
        ncms_iguais.append(ncm_planilha)
    else:
        ncms_diferentes.append(ncm_planilha)

# Gravação dos resultados em arquivos
grava_arquivo('NCMsNaoEncontrados.txt', ncms_diferentes)
grava_arquivo('NCMsEncontrados.txt', ncms_iguais)

print(f"{len(planilha)} NCMS da Planilha analisados e comparados com os {len(ncms_api)} NCMS da API.")
print(f"{len(ncms_diferentes)} NCMS não foi/foram encontrado(s) na API.")
print(f"{len(ncms_iguais)} NCMS foi/foram encontrado(s) na API.")
print("Resultados gravados nos arquivos NCMsNaoEncontrados.txt e NCMsEncontrados.txt.")
