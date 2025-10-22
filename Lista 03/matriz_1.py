matriz_1 = []
print("Digite os elementos da matriz 2x2:")
for i in range(2):
    linha = []
    for j in range(2):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_1.append(linha)

print("\nMatriz digitada:")
for linha in matriz_1:
    print(linha)