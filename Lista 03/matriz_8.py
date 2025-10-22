matriz_8 = []
print("Digite os elementos da matriz 2x2 (números reais):")
for i in range(2):
    linha = []
    for j in range(2):
        num = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_8.append(linha)

print("\nMatriz 2x2 (reais):")
for linha in matriz_8:
    print(linha)