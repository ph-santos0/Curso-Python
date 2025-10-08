positivos = negativos = zeros = contador = 0
while contador < 20:
    numero = float(input('Digite um número: '))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1
    contador += 1
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(f'Zeros: {zeros}')
