def combinacao(objetos, ordem):
    if ordem == 0:
        return 1
    elif objetos == ordem:
        return 1
    elif objetos < ordem:
        return 0
    return combinacao(objetos - 1, ordem) + combinacao(objetos - 1, ordem - 1)


print(combinacao(100, 50))
