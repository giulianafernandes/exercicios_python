"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while."""
n = int(input('Insira o número onde começa a sua Progressão Aritmética: '))
r = int(input('Insira a razão: '))
c = 1
while c <= 10:
  n += r
  c += 1
  print(n ,end='')
  print(', ' if c <= 10 else '.' , end='')