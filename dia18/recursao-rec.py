def rec(n):
    print(n)
    if n > 0:
        rec(n-1)


def recInverso(n):
    if n > 0:
        rec(n-1)
    print(n)


rec(5)
print("------------")
recInverso(5)
