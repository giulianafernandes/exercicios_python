"""
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
cont = 0
n = 0
soma = 0
while n != 999:
  n = int(input('Digite um número inteiro: \n• Para parar, digite 999 • '))
  if n != 999:
    soma += n
    cont += 1
  else:
    print(f'Você digitou {cont} números que somados resultam em {soma}')
    print('!fim!')