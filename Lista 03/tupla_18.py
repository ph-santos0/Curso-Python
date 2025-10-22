notas_alunos = ((7, 8, 6), (9, 5, 7), (8, 8, 10))
print(f"Tupla aninhada de notas: {notas_alunos}")
nota_2_aluno_1 = notas_alunos[1][0]
print(f"Primeira nota do segundo aluno: {nota_2_aluno_1}")
notas_terceiro_aluno = notas_alunos[2]
media_terceiro_aluno = sum(notas_terceiro_aluno) / len(notas_terceiro_aluno)
print(f"Média do terceiro aluno: {media_terceiro_aluno:.2f}")