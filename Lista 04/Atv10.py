import math 

try:
    num_str = input("Digite um número: ")
    numero = float(num_str)
    
    if numero < 0:
        raise ValueError("A idade não pode ser negativa!")
        
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz}")

except ValueError as e:
    if "negativa" in str(e):
        print("Erro: não é possível calcular raiz de número negativo.")
    else:
        print("Erro: você não digitou um número válido.")