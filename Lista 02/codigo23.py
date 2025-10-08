import random
numero_secreto = random.randint(1, 10)
tentativas = 0
chute = 0
while chute != numero_secreto:
    chute = int(input('Adivinhe o número entre 1 e 10: '))
    tentativas += 1
    if chute < numero_secreto:
        print('Tente um número maior.')
    elif chute > numero_secreto:
        print('Tente um número menor.')
print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.')
