# Autor: Pedro Henrique Santos
idade = int(input("Digite a idade da pessoa: "))
if idade < 16:
    print("Classe eleitoral: Não eleitor")
elif (idade >= 16 and idade < 18) or idade >= 65:
    print("Classe eleitoral: Eleitor facultativo")
else:
    print("Classe eleitoral: Eleitor obrigatório")