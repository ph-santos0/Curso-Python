soma_notas = quantidade_notas = 0
nota = 0
while nota != -1:
    nota = float(input('Digite uma nota (0 a 10) ou -1 para sair: '))
    if 0 <= nota <= 10:
        soma_notas += nota
        quantidade_notas += 1
    elif nota != -1:
        print('Nota inválida. Digite uma nota entre 0 e 10.')
if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f'A média das notas válidas é: {media:.2f}')
else:
    print('Nenhuma nota válida foi digitada.')
