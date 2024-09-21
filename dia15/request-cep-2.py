import requests

print("-=" * 20)
cep = str(input("Digite seu CEP: "))
numero = int(input("Digite o número do logradouro: "))

url = f'https://viacep.com.br/ws/{cep}/json/'

endereco = requests.get(url)

local = endereco.json()

if local['complemento'] == '':
    print(f"Você mora na {local['logradouro']} {numero}, {local['bairro']} - {local['localidade']}, {local['estado']}")
else:
    print(f"Você mora na {local['logradouro']} {numero}, {local['bairro']} - {local['localidade']}, {local['estado']} (Complemento: {local["complemento"]})")

print("-=" * 20)
# Extraindo a string e um JSON (formato de dicionário)
