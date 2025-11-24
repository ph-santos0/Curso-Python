def media(notas):
    return sum(notas) / len(notas)


notas = []

print("Digite 3 notas do alunos:")
for i in range(3):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

if media(notas) >= 7:
    print("Aprovado")
elif media(notas) >= 5:
    print("Recuperação")
else:
    print("Reprovado")


media_lambda = lambda notas: sum(notas) / len(notas)


if media_lambda(notas) >= 7:
    print("Aprovado (usando lambda)")
elif media_lambda(notas) >= 5:
    print("Recuperação (usando lambda)")
else:
    print("Reprovado (usando lambda)")
