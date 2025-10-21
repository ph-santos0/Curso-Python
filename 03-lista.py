frutas = ["maçã", "banana", "laranja"]
print(frutas)

f2 = frutas[1]
print(f2)

frutas.append("uva")
print(frutas)

frutas.insert(1, "abacaxi")
print(frutas)

frutas.remove("banana")
print(frutas)

del frutas[0]
print(frutas)

numeros = [10, 20, 30, 40, 50]
l2 = numeros[1:4]
print(l2)

print(numeros[:3])

print(numeros[-2:])

lista1 = [1, 2, 3]
lista2 = [4, 5]
lista3 = lista1 + lista2
print(lista3)

idades = [25, 30, 35, 20]
print(idades)
print(len(idades))
print(max(idades))
print(min(idades))
print(sum(idades))
print(sorted(idades))

t = 3 * idades
print(t)

if 20 in idades:
    print("20 está na lista")
else:
    print("20 não está na lista")