import requests

url = 'https://viacep.com.br/ws/09041010/json/'

r = requests.get(url)
print(r.text)
print(r.json())

cep = r.json()
print(cep['bairro'])

# Extraindo a string e um JSON (formato de dicionário)
