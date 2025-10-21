aluno = {
    "nome": "Pedro",
    "idade": 20,
    "curso": "BSI"
}

print(aluno)
print(aluno["nome"])
print(aluno["idade"])

aluno["idade"] = 21
print(aluno)

aluno["matricula"] = "0077113"
print(aluno)

del aluno["curso"]
print(aluno)

matricula = aluno.pop("matricula")
print(matricula)
print(aluno)

if "idade" in aluno:
    print("Idade está no dicionário")
else:
    print("Idade não está no dicionário")

if "matricula" in aluno:
    print("Curso está no dicionário")
else:
    print("Curso não está no dicionário")


print(aluno.keys())

alunos = [
    {"nome": "Ana", "idade": 22, "curso": "Engenharia"},
    {"nome": "Beatriz", "idade": 21, "curso": "Medicina"}
]

alunos.append({"nome": "Carlos", "idade": 23, "curso": "Direito"})
print(alunos)

ponto = {"x": 10, "y": 20}
print(ponto)
print(ponto.values())
print(ponto.items())
print(ponto["x"], ponto["y"])
