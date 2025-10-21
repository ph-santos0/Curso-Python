numeros = {1, 2, 3, 4, 5}
print(numeros)
numeros.add(6)
print(numeros)
numeros.remove(3)
print(numeros)

numeros.discard(3)
print(numeros)

numeros.clear()
print(numeros)

pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

# uniao
u = pares | impares
print(u)

p2 = {4, 5, 6}

# interseccao
i = pares & p2
print(i)

p3 = {2, 6}

# diferenca
d = pares - p3
print(d)

p4 = {4, 6, 10}

# diferenca simetrica
s = pares ^ p4
print(s)
