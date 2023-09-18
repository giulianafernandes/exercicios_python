"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1.
"""
print('='*7, 'Giulianas Bank', '='*7)
valor = int(input('Digite o valor a ser sacado: '))
cedula = 50
total_cedula = 0
total = valor

while True:
  if total >= cedula:
    total -= cedula
    total_cedula += 1
  else:
    print(f'Total de {total_cedula} cédulas de R${cedula}')
    if cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    total_cedula = 0

    if total == 0:
      break