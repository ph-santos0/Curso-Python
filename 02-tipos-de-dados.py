nome = "Pedro"  # string
idade = 21  # inteiro
altura = 1.92  # float
estudante = True  # booleano
notas = [8.5, 9.0, 7.5]  # lista
numeros = (1, 2, 3, 4, 5)  # tupla
aluno = {"nome": "Isadora", "idade": 19, "curso": "Fisioterapia"}  # dicionario
cores = {"vermelho", "verde", "azul"}  # conjunto

print("Nome: " + nome + "\nIdade: " + str(idade) + "\nAltura: " +
      str(altura) + "\nEstudante: " + str(estudante))
print(
    f"\nNome: {nome}\nIdade: {idade}\nAltura: {altura}\nEstudante: {estudante}")

print("\nNome:", nome, "\nIdade:", idade, "\nAltura:",
      altura, "\nEstudante:", estudante)

print ("\nNotas:", notas)
print("Numeros:", numeros)
print("Aluno:", aluno)
print("Cores:", cores)