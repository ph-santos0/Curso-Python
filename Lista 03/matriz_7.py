matriz_7 = []
print("Digite os elementos (nomes ou letras) da matriz 2x3:")
for i in range(2):
    linha = []
    for j in range(3):
        texto = input(f"Elemento [{i}][{j}]: ")
        linha.append(texto)
    matriz_7.append(linha)

print("\nMatriz 2x3 digitada:")
for linha in matriz_7:
    print(linha)