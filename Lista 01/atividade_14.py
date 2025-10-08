# Autor: Pedro Henrique Santos
idade = int(input("Digite a idade da pessoa: "))
if idade < 18:
    print("Classificação: Menor de idade")
elif idade >= 65:
    print("Classificação: Pessoa idosa")
else:
    print("Classificação: Maior de idade")