matriz_3 = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_3.append(linha)

print("\nSoma das linhas:")
for i in range(3):
    soma_linha = sum(matriz_3[i])
    print(f"Soma da Linha {i}: {soma_linha}")