matriz_5 = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_5.append(linha)

soma_dp = 0
soma_ds = 0
for i in range(3):
    soma_dp += matriz_5[i][i]
    soma_ds += matriz_5[i][2 - i]

print(f"\nSoma da Diagonal Principal: {soma_dp}")
print(f"Soma da Diagonal Secundária: {soma_ds}")