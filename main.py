import firebase_admin
from firebase_admin import credentials, db
import csv
import time

# Conectar ao Firebase
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://extensao-estacio-dbfcd-default-rtdb.firebaseio.com/'
})

# Função para ler dados do arquivo CSV
def ler_dados_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            dados.append({
                'operador': linha['operador'],
                'tempo_atendimento': float(linha['tempo_atendimento']),
                'tempo_inatividade': float(linha['tempo_inatividade'])
            })
    return dados

# Ler dados do arquivo CSV
dados_operadores = ler_dados_csv('dados_operadores.csv')


for dados in dados_operadores:
    # Enviar os dados para o Firebase
    ref = db.reference('/performance')
    ref.push(dados)
    
    print(f'Dados enviados: {dados}')
    time.sleep(1)  

print("Dados coletados e armazenados com sucesso no Firebase!")
