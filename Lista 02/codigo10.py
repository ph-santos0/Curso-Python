soma_positivos = 0
total_negativos = 0
for _ in range(20):
    numero = float(input('Digite um número: '))
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        total_negativos += 1
print(f'Soma dos positivos: {soma_positivos}')
print(f'Total de números negativos: {total_negativos}')
