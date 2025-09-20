# Questao 1
print("Estou aprendendo Python!")

# Questao 2
nome = "Pedro"
idade = 21
print("Meu nome é", nome, "e tenho", idade, "anos.")

# Questao 3
a = 5
b = 10
soma: int = a + b
subtracao: int = b - a
multiplicacao: int = a * b
divisao: int = b / a
print("Calculando a =", a, "e b =", b)
print("Soma:", soma)
print("Subtracao:", subtracao)
print("Multiplicacao:", multiplicacao)
print("Divisao:", divisao)

# Questao 4
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("Olá", nome, "! Você tem", idade, "anos.")

# Questao 5
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma: int = num1 + num2
print("A soma e", soma)

# Questao 6
num = int(input("Digite um número: "))
print("O dobro de", num, "é", num * 2)
print("O triplo de", num, "é", num * 3)
print("A metade de", num, "é", num / 2)

# Questao 7
reais = float(input("Digite um valor em reais: "))
dolares = reais / 5
print("O valor em dólares é:", dolares)

# Questao 8
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
print("Olá", nome, "! Você tem", idade, "anos e mora em", cidade + ".")

# Questao 9
print("Insira as duas notas:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
print("A media é:", media)
if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperacao")
else:
    print("Reprovado")
