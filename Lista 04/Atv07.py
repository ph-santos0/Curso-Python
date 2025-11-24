def dividir(num1, num2):
    return num1 / num2

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = dividir(numero1, numero2)
    print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Erro: Você deve digitar números válidos.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
    