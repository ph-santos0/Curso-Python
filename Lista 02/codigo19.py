dias_semana = {1: 'Domingo', 2: 'Segunda-feira', 3: 'Terça-feira', 4: 'Quarta-feira', 5: 'Quinta-feira', 6: 'Sexta-feira', 7: 'Sábado'}
contador = 0
while contador < 5:
    numero_dia = int(input('Digite um número de 1 a 7: '))
    if 1 <= numero_dia <= 7:
        print(f'O dia da semana é: {dias_semana[numero_dia]}')
        contador += 1
    else:
        print('Número inválido. Digite um número entre 1 e 7.')
