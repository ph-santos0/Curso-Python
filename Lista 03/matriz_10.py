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

matriz_mult = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        soma_prod = 0
        for k in range(2):
            soma_prod += matriz_A[i][k] * matriz_B[k][j]
        matriz_mult[i][j] = soma_prod

print("\nMatriz Multiplicação (A * B):")
for linha in matriz_mult:
    print(linha)