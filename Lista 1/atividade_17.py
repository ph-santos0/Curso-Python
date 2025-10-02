# Autor: Pedro Henrique Santos
numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
if numero_mes in meses:
    print(f"O mês correspondente é: {meses[numero_mes]}")
else:
    print("Não existe mês com este número. Por favor, digite um número entre 1 e 12.")