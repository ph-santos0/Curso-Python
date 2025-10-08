num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = 0
if num1 < num2:
    for i in range(num1 + 1, num2):
        soma += i
else:
    for i in range(num2 + 1, num1):
        soma += i
print(f'A soma dos números entre eles é: {soma}')
