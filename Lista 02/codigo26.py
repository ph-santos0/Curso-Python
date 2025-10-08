while True:
    try:
        n = int(input('Quantas idades você vai digitar? '))
        if n <= 0:
            print('Por favor, digite um número positivo de idades.')
            continue
        break
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
menores = adultos = idosos = contador = 0
while contador < n:
    try:
        idade = int(input(f'Digite a {contador+1}ª idade: '))
        if idade < 0:
            print('Idade inválida. Digite uma idade positiva.')
            continue
        if idade < 18:
            menores += 1
        elif idade >= 60:
            idosos += 1
        else:
            adultos += 1
        contador += 1
    except ValueError:
        print('Entrada inválida. Digite um número inteiro para a idade.')
print('Faixa etária:')
print(f'Menores de 18 anos: {menores}')
print(f'Adultos (18 a 59 anos): {adultos}')
print(f'Idosos (60 anos ou mais): {idosos}')
