"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
tot_produto = mil = cont = nome_maisbarato = 0
while True:
  nome = str(input('Digite o nome do produto: ')).strip().lower()
  preço = float(input('Agora digite o preço do produto: '))
  continuar = str(input('Deseja continuar?[S/N] ')).strip().lower()[0]
  soma += preço
  cont += 1

  if preço >= 1000:
    mil += 1

  if cont == 1:
    menor = preço
    nome_maisbarato = nome
  elif preço < menor:
    menor = preço
    nome_maisbarato = nome

  if continuar == 'n':
    break

print(f'O total gasto é de R${soma}.')
print(f'{mil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato é {nome_maisbarato}.')