def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    return fibonacci(numero - 1) + fibonacci(numero - 2)


for i in range(0, 100):
    print(fibonacci(i))
