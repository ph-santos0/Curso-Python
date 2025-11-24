p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

p1_low = p1.lower()
p2_low = p2.lower()

if p1_low == p2_low:
    print("As palavras são exatamente iguais.")

elif sorted(p1_low) == sorted(p2_low): 
    print("As palavras são anagramas.")
    
else:
    print("As palavras são completamente diferentes.")