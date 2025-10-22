matriz_4 = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_4.append(linha)

print("\nSoma das colunas:")
for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna += matriz_4[i][j]
    print(f"Soma da Coluna {j}: {soma_coluna}")