# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num+1):
  if num % c == 0:
    print(f'{num} é divisível por {c}.')
    total += 1
  else:
    print(f'{num} não é divisível por {c}.')

if total == 2:
  print(f'{num} é um número primo!')
else:
  print(f'{num} não é um número primo!')