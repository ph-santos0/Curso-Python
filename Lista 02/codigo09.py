num_total = int(input('Quantos números você vai digitar? '))
maior = 0
for i in range(num_total):
    numero = float(input(f'Digite o {i+1}º número: '))
    if numero > maior:
        maior = numero
print(f'O maior número é: {maior}')
