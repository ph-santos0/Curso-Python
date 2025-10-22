matriz_2 = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz_2.append(linha)

print("\nMatriz 3x3 (formato tabela):")
for linha in matriz_2:
    for elemento in linha:
        print(f" {elemento:^5} ", end="")
    print()