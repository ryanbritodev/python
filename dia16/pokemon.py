import requests

# https://pokeapi.co

nomePokemon = str(input("Digite o nome do Pokemon que você deseja ver: ")).strip().lower()

url = f"https://pokeapi.co/api/v2/pokemon/{nomePokemon}"

json = requests.get(url)

pokemon = json.json()

print(f"O ID do seu Pokemon ({nomePokemon.title()}) é {pokemon['id']}")
print(f"O tipo dele é {pokemon['types'][0]['type']['name']}")
