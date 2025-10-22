print("--- Matriz A (2x2) ---")
matriz_A = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(float(input(f"A[{i}][{j}]: ")))
    matriz_A.append(linha)

print("--- Matriz B (2x2) ---")
matriz_B = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(float(input(f"B[{i}][{j}]: ")))
    matriz_B.append(linha)

matriz_soma = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        matriz_soma[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("\nMatriz Soma (A + B):")
for linha in matriz_soma:
    print(linha)