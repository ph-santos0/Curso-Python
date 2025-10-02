# Autor: Pedro Henrique Santos
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 20:
    print("Situação: Abaixo do peso")
elif 20 <= imc < 25:
    print("Situação: Peso normal")
elif 25 <= imc < 30:
    print("Situação: Sobre peso")
elif 30 <= imc < 40:
    print("Situação: Obeso")
else:
    print("Situação: Obeso Mórbido")