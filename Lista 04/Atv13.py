primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = f"{primeiro_nome} {sobrenome}" 

print(f"Maiúsculas: {nome_completo.upper()}")
print(f"Minúsculas: {nome_completo.lower()}")
print(f"Capitalizado: {nome_completo.title()}")