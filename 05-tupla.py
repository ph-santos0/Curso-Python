coordenada = (10, 20)

print(coordenada)
print(coordenada[0])
print(coordenada[1])

cores = ("vermelho", "verde", "azul", "verde")

print(len(cores))  # Tamanho da tupla
print(cores.count("verde"))  # Conta quantas vezes "verde" aparece
i = cores.index("azul")
print(i)

print(cores[1:3])  # Fatiamento
print(cores[:2])  # Fatiamento
print(cores[-2:])  # Fatiamento

ponto = (99, 200)

x, y = ponto
# Desempacotamento
print(x)
print(y)

t = (10, 20, (30, 40))
print(t[2][1])  # Acessando elemento dentro da tupla aninhada

t1 = (1, 2, 3)
t2 = (4, 5)
r = t1 + t2  # Concatenação
print(r)
t3 = t1 * 2  # Repetição
print(t3)

if "verde" in cores:
    print("verde está na tupla")
else:
    print("verde não está na tupla")