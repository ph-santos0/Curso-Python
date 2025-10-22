matriz_6 = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_6.append(linha)

somas = []

soma_dp = 0
soma_ds = 0
for i in range(3):
    soma_dp += matriz_6[i][i]
    soma_ds += matriz_6[i][2 - i]
somas.append(soma_dp)
somas.append(soma_ds)

for i in range(3):
    somas.append(sum(matriz_6[i]))

for j in range(3):
    soma_col = 0
    for i in range(3):
        soma_col += matriz_6[i][j]
    somas.append(soma_col)

eh_magico = True
primeira_soma = somas[0]
for soma in somas:
    if soma != primeira_soma:
        eh_magico = False
        break

if eh_magico:
    print(f"\nÉ um quadrado mágico! (Soma = {primeira_soma})")
else:
    print(f"\nNão é um quadrado mágico. Somas: {somas}")