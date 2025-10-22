alunos_disciplinas = {
    "Ana": {"Matemática", "Física"},
    "Bruno": {"Geografia", "História"},
    "Carla": {"Matemática", "História"}
}

disciplinas_ana = alunos_disciplinas["Ana"]
disciplinas_carla = alunos_disciplinas["Carla"]

uniao_disciplinas = disciplinas_ana.union(disciplinas_carla)

print(f"Disciplinas de Ana: {disciplinas_ana}")
print(f"Disciplinas de Carla: {disciplinas_carla}")
print(f"União (Ana e Carla): {uniao_disciplinas}")