numero = int(input('Digite um número: '))
if numero <= 1:
    print(f'{numero} não é primo.')
else:
    is_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break
    if is_primo:
        print(f'{numero} é primo.')
    else:
        print(f'{numero} não é primo.')
