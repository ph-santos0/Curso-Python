frase = input("Digite uma frase: ")

palavras = frase.split()

print("\n--- Palavras na frase ---")
for palavra in palavras:
    print(palavra) #

print(f"\nTotal de palavras: {len(palavras)}")