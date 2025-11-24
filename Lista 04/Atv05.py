def conversor(c):
    return c * 1.8 + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = conversor(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

fahrenheit = lambda c: c * 1.8 + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit(celsius)}")