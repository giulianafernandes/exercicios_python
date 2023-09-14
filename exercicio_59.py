"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
operação = 0

while operação != 5:
  print('Agora selecione a operação que deseja realizar.')
  print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
  operação = int(input(''))
  if operação == 1:
    print(f'A soma dos números {n1}+{n2}={n1+n2}.')
  elif operação == 2:
    print(f'A multiplicação dos números {n1}x{n2}={n1*n2}.')
  elif operação == 3:
      if n1 > n2:
        print(f'{n1} é maior que {n2}')
      elif n2 > n1:
        print(f'{n2} é maior que {n1}')
      else:
        print('Os valores são iguais.')
  elif operação == 4:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
  elif operação not in [1,2,3,4,5]:
    print('O valor digitado é inválido, tente novamente.')
print('!fim!')