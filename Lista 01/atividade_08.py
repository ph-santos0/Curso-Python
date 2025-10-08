# Autor: Pedro Henrique Santos
numero_a = int(input("Digite o primeiro número (A): "))
numero_b = int(input("Digite o segundo número (B): "))
if numero_b != 0:
    if numero_a % numero_b == 0:
        print(f"{numero_a} é divisível por {numero_b}")
    else:
        print(f"{numero_a} não é divisível por {numero_b}")
else:
    print("Não é possível dividir por zero.")