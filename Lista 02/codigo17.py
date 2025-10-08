count = 0
for _ in range(10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0 and numero % 5 == 0:
        count += 1
print(f'Quantidade de números pares e múltiplos de 5: {count}')
