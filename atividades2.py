#Questao 1
print("Questão 1")
contador = 0
print(f"Valor inicial de contador: {contador}")
contador += 1
print(f"Novo valor do contador: {contador}")
contador -= 1
print(f"Valor final do contador: {contador}")

#Questao 2
print("\nQuestão 2")
preco = 2.50
qtd = 4
total = preco * qtd
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade comprada: {qtd}")
print(f"Total a pagar: R$ {total:.2f}")

#Questao 3
print("\nQuestão 3")
A = 10
B = 20
print(f"Valor inicial de A: {A}")
print(f"Valor inicial de B: {B}")
A, B = B, A
print(f"Novo valor de A: {A}")
print(f"Novo valor de B: {B}")

#Questao 4
print("\nQuestão 4")
num = input("Digite um numero: ")
print(f"Tipo de variavel numero antes de conversão: {type(num)}")
num = int(num)
num = num * 2
print(f"O dobro do numero é: {num}")

#Questao 5
print("\nQuestão 5")
numfloat = 15.75
print(f"Numero float = {numfloat}")
print(f"Tipo de variavel antes de conversão: {type(numfloat)}")
numint = str(numfloat)
print(f"Tipo de variavel depois da conversão: {type(numint)}")
print(f"{numint} e um numero do tipo string")

#Questao 6
print("\nQuestão 6")
nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (ex: 1.75): "))
print(f"{nome} tem {idade} anos e {altura:.2f} de altura.")