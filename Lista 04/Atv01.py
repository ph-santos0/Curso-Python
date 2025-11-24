def soma_pares(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a + b
    else:
        return 0


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(soma_pares(a, b))


soma_pares_lambda = lambda a, b: a + b if a % 2 == 0 and b % 2 == 0 else 0
print(soma_pares_lambda(a, b))
