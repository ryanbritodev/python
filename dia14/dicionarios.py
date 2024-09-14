dict = {
    "Nome": "Helder",
    "Idade": 33,
    "Cabeludo": True,
    ("Cássio", "Ramos", 12): True
}

dict["Professor"] = True
print(dict)
print(type(dict))
print("asd" in dict)
print(dict.get("Idade")) # Se não tiver, retorna None
print(dict["Nome"])
print(dict[("Cássio", "Ramos", 12)])
print(len(dict["Idade"]))

print(dict.values())

del dict["Cabeludo"]
# ou
print(dict.pop("Idade"))

# Atualiza chaves em comum, sobrescrevendo os valores
# dicionarioA.update(dicionarioB)
