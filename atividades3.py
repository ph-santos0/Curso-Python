print("Pagamento Academia")
pagamento = float(input("Insira o valor pago pelo aluno:"))

if pagamento < 100:
    diferenca = 100-pagamento
    devedor = diferenca + diferenca * 0.1
    print("Pagou menos que a mensalidade, saldo devedor com a multa: ", devedor)

elif pagamento > 100:
    diferenca = pagamento - 100
    print("Troco: ", diferenca)

else:
    print("Mensalidade paga!")
    