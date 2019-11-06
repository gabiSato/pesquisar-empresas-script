import requests

url = "https://www.receitaws.com.br/v1/cnpj/"

def transform_response(response):
    return {
        "nome": response["nome"],
        "email": response["email"],
        "telefone": response["telefone"],
        "uf": response["uf"],
        "data_de_abertura": response["abertura"],
        "atividades_secundarias": response["atividades_secundarias"],
    }

def display_info(data):
    for name, value in data.items():
        print(name, ": ", value)

def search_company(cnpj):
    response = requests.get(url + cnpj).json()
    data = transform_response(response)
    display_info(data)

option = -1

while(option != 0):
    option = int(input("Digite 1 para pesquisar empresa ou 0 para sair: "))
    if (option == 1):
        cnpj = input("Digite o cnpj da empresa: ")
        search_company(cnpj)