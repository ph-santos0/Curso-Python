while True:
    try:
        texto = input("Digite um número inteiro: ")
        numero = int(texto)

        print(f"Número digitado: {numero}")
        break

    except ValueError:
        print("Erro: você não digitou um número inteiro. Tente novamente.")
