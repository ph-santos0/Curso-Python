print("--- Cadastro do Gabarito da Mega Sena ---")
gabarito = []
for i in range(6):
    num = int(input(f"Digite o {i + 1}º número do gabarito: "))
    gabarito.append(num)

print("\n--- Leitura das Apostas ---")
for i in range(10):
    print(f"\n--- Aposta {i + 1} ---")
    aposta_atual = []
    for j in range(6):
        num_aposta = int(input(f"Digite o {j + 1}º número da aposta: "))
        aposta_atual.append(num_aposta)

    acertos = 0
    for numero in aposta_atual:
        if numero in gabarito:
            acertos += 1

    print(f"Aposta {i + 1} teve: {acertos} acertos.")

    if acertos == 4:
        print("Resultado: QUADRA")
    elif acertos == 5:
        print("Resultado: QUINA")
    elif acertos == 6:
        print("Resultado: SENA")