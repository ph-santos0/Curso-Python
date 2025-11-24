try:
    nome = input("Digite o nome: ")
    idade_str = input("Digite a idade: ")
    nota_str = input("Digite a nota final: ")

    idade = int(idade_str)
    nota = float(nota_str)

    if not (0 <= nota <= 10):
        print(f"Aviso: A nota {nota} está fora do intervalo de 0 a 10.")
    
    print("\n--- Aluno Cadastrado ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}")

except ValueError:
    print("Erro: Idade e Nota devem ser valores numéricos válidos.")