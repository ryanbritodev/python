def f(x):
    if x < -2:
        return x ** 2 + 3 * x - 4
    elif x < 0:
        return 2*x + 5
    elif x < 4:
        return x ** 0.5
    elif x < 6:
        return x ** 3 - 3 * x ** 2 - 10 * x
    elif x < 8:
        return 3 * x ** 2 - 4 * x - 20
    else:
        return 10


print(f(7))
