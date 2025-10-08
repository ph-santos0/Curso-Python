soma_acumulada = 0
quantidade_numeros = 0
while soma_acumulada <= 100:
    numero = float(input('Digite um número: '))
    soma_acumulada += numero
    quantidade_numeros += 1
print(f'Soma acumulada: {soma_acumulada}')
print(f'Quantidade de números lidos: {quantidade_numeros}')
