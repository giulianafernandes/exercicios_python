# exercicio 044 - Gerenciador de Pagamentos

valor = float(input('Digite o valor do produto: '))
print('Opções de pagamento:')
print('[1] - à vista dinheiro/cheque: 10% de desconto')
print('[2] - à vista no cartão: 5% de desconto')
print('[3] - em até 2x no cartão: preço normal')
print('[4] - 3x ou mais no cartão: 20% de juros')

pagamento = int(input('Digite a forma de pagamento: '))

print(f'Sua compra é de R${valor:.2f}')

if pagamento == 1:
  print(f'Com desconto de 10% à vista no dinheiro ou cheque, a compra fica R${valor - (0.1*valor):.2f}')
elif pagamento == 2:
  print(f'Com desconto de 5% à vista no cartão, a compra fica R${valor-(0.05*valor):.2f}')
elif pagamento == 3:
  print('Em até 2x no cartão não se aplica desconto.')
elif pagamento == 4:
  print(f'Em 3x no cartão você paga 20% de juros, então sua compra fica R${valor+(0.2*valor):.2f}')