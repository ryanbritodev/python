import requests

# Como pegar o HTML de uma URL e verificar a resposta da requisição

url = "https://www.fiap.com.br/"

r = requests.get(url)
print(r)
print(r.text)
