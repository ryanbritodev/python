import requests

url = 'https://apis.codante.io/olympic-games/countries'

objeto = requests.get(url).json()

pais = str(input("Digite o nome do país: ")).strip()

medalhas = objeto['data']

for dicionario in medalhas:
    if pais != dicionario['name']:
        continue
    print("LISTA DE MEDALHAS {}".format(pais.upper()))
    print(f"🥇 Ouros: {dicionario["gold_medals"]}")
    print(f"🥈 Pratas: {dicionario["silver_medals"]}")
    print(f"🥉 Bronzes: {dicionario["bronze_medals"]}")

# Extraindo a string e um JSON (formato de dicionário)
