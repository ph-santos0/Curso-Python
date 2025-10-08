base = float(input('Digite a base (A): '))
expoente = int(input('Digite o expoente (B, inteiro e positivo): '))
resultado = 1
for _ in range(expoente):
    resultado *= base
print(f'O resultado de {base}^{expoente} é: {resultado}')
