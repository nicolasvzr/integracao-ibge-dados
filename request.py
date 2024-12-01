import requests
import mysql.connector
from conDB import conexao
from tabulate import tabulate

nome = 'João'
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

#params = {'localidade': 33}

response = requests.get(url = url )

if response.status_code == 200:
    data = response.json()[0]['res']
    #print(tabulate(data, headers= "keys", tablefmt="pretty"))
    print("Dados extraídos com sucesso.")
else:
    print(f"Erro ao acessar a API: {response.status_code}")


print(tabulate(data, headers= "keys", tablefmt="pretty"))

conexao_bd = conexao()

cursor = conexao_bd.cursor()


#Manipulação

frequencias = []
periodos_processados = set()

if data:
    for registro in data:
        decada = registro['periodo'].strip("[]") #Limpeza dos dados
        frequencia = registro['frequencia']

        if decada not in periodos_processados:
            frequencias.append((decada, frequencia))
            periodos_processados.add(decada)
        



for decada, frequencia in frequencias:
        cursor.execute(
                "INSERT INTO frequencias (decada, frequencia) VALUES (%s, %s)",
                (decada, frequencia)
        )

conexao_bd.commit()
print("Dados inseridos com sucesso")

        
cursor.close()
conexao_bd.close()

