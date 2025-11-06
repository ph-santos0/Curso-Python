lista = []


def quadrado(lista):
    lista2 = []
    for numero in lista:
        lista2.append(numero ** 2)
    return lista2


for i in range(3):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

print("Lista original:", lista)
print(quadrado(lista))

quadrado_map = list(map(lambda x: x ** 2, lista))
print("Lista ao quadrado usando map e lambda:", quadrado_map)
