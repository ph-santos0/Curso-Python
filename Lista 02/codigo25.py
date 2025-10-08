total_compra = 0
while True:
    valor_item = float(input('Digite o valor do item (0 para finalizar): '))
    if valor_item == 0:
        break
    total_compra += valor_item
print(f'Total da compra: R$ {total_compra:.2f}')
valor_pago = float(input('Digite o valor pago: R$ '))
troco = valor_pago - total_compra
if troco >= 0:
    print(f'Troco: R$ {troco:.2f}')
else:
    print('Valor pago insuficiente.')
