frase = input("Digite uma frase: ")

contagem_a = frase.lower().count('a')
print(f"A letra 'a' aparece {contagem_a} vezes.")

palavras = frase.split()
print(f"A frase tem {len(palavras)} palavras.")