# Autor: Pedro Henrique Santos
salario_bruto = float(input("Digite o salário bruto: "))
valor_prestacao = float(input("Digite o valor da prestação desejada: "))
limite_prestacao = 0.30 * salario_bruto
if valor_prestacao <= limite_prestacao:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NÃO CONCEDIDO. O valor da prestação excede 30% do salário bruto.")