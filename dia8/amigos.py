def divisores(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma


def amigos(a, b):
    if divisores(b) == a and divisores(a) == b:
        return True
    else:
        return False


print(amigos(284, 220))
