# Autor: Pedro Henrique Santos
idade = int(input("Digite a idade da pessoa: "))
if idade <= 10:
    valor_plano = 100.00
elif idade <= 30:
    valor_plano = 150.00
elif idade <= 50:
    valor_plano = 250.00
else:
    valor_plano = 400.00
print(f"O valor a ser pago pelo plano de saúde é: R$ {valor_plano:.2f}")