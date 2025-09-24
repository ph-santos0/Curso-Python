#Conversões
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)

print(f"Meu nome e {nome} e tenho {idade} anos.")
print(f"Daqui 1 ano voce tera {idade + 1} anos.")
print(f"Tipo de variavel nome: {type(nome)}")
print(f"Tipo de variavel idade: {type(idade)}")

altura = input("Digite sua altura (ex: 1.75): ")
print(f"Tipo de variavel altura antes de conversão: {type(altura)}")
altura = float(altura)
print(f"Tipo de variavel altura depois da conversão: {type(altura)}")

numero = 100
print("Numero = 100")
print(f"Tipo de variavel numero antes de conversão: {type(numero)}")
numero = str(numero)
print(f"Tipo de variavel numero depois da conversão: {type(numero)}")

boleana = ""
print(bool(boleana))
boleana = "a"
print(bool(boleana))

# Constantes e Variaveis
idade = 30
print(f"Idade inicial: {idade}")
idade = 31
print(f"Idade atualizada: {idade}")

PI = 3.14159
TAXAJUROS = 0.05

print(f"O valor de PI: {PI}")
print(f"A taxa de juros: {TAXAJUROS}")