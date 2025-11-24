def maior_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = maior_de_tres(num1, num2, num3)
print(f"O maior número é: {maior}")

maior_lambda = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)
print(f"O maior número é: {maior}")