idades = []


def maioridade(idades):
    maioridades = []
    for idade in idades:
        if idade >= 18:
            maioridades.append(idade)
    return maioridades


for i in range(5):
    n = int(input("Digite a idade: "))
    idades.append(n)

print("Idades maiores ou iguais a 18 anos:", maioridade(idades))

maioridades_lambda = list(filter(lambda idade: idade >= 18, idades))

print("Idades maiores ou iguais a 18 anos (usando filter e lambda):", maioridades_lambda)
