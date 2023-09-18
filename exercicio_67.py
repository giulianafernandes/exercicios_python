"""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
print('~•*'*5,'TABUADA','*•~'*5)
n = int(input('Digite um número:'))
cont = 0
p = 1
while True:
  print(f'{n} x {p} = {n*p}')
  p += 1
  cont += 1
  if cont == 10:
    break
  if n < 0:
    break
print('!fim!')