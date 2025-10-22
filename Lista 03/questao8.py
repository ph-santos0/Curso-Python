tupla_7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Tupla original: {tupla_7}")

lista_7 = list(tupla_7)
print(f"Convertido para lista: {lista_7}")

lista_7.append(11)
print(f"Lista após adicionar 11: {lista_7}")

tupla_final_7 = tuple(lista_7)
print(f"Convertido para tupla final: {tupla_final_7}")