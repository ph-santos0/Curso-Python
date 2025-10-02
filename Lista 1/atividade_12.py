# Autor: Pedro Henrique Santos
valores = []
valores.append(float(input("Digite o primeiro valor (A): ")))
valores.append(float(input("Digite o segundo valor (B): ")))
valores.append(float(input("Digite o terceiro valor (C): ")))
valores.sort(reverse=True)
print("Valores em ordem descendente:", valores)