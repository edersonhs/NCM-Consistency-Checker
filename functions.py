import requests

def carregar_dados_ncms(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro para respostas inválidas
    return response.json()

def otimizar_ncm_data(ncms_data):
    codigos_ncm = []
    for item in ncms_data['Nomenclaturas']:
        if "Codigo" in item:
            codigo_sem_pontos = item["Codigo"].replace('.', '').strip()
            if len(codigo_sem_pontos) == 8:
                codigos_ncm.append(codigo_sem_pontos)
    return codigos_ncm

def grava_arquivo(nome_arquivo, dados):
    file = open(nome_arquivo, 'w')
    for dado in dados:
        file.write(str(dado) + '\n')
    file.close()
