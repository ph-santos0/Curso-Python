# Autor: Pedro Henrique Santos
numero_a = float(input("Digite o primeiro número (A): "))
numero_b = float(input("Digite o segundo número (B): "))
if numero_a > numero_b:
    print(f"O maior valor é: {numero_a}")
    print(f"O menor valor é: {numero_b}")
elif numero_b > numero_a:
    print(f"O maior valor é: {numero_b}")
    print(f"O menor valor é: {numero_a}")
else:
    print("Os números são iguais.")