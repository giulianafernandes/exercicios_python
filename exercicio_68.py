"""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('=-'*5, 'VAMOS JOGAR!', '=-'*5)
cont = 0
while True:
  escolha = str(input('Você escolhe PAR ou ÍMPAR? ')).strip().lower()[0]
  n = int(input('Digite o seu número!: '))
  npc = randint(0,10)
  if escolha in 'ií':
    print('você escolheu Ímpar, eu escolho Par!')
  elif escolha == 'p':
    print('você escolheu Par, eu escolho Ímpar!')
  resultado = n + npc
  cont += 1
  print(f'Você escolheu {n}, eu escolhi {npc}!')
  if escolha == 'p' and resultado % 2 == 0:
    print(f'Ahhhh droga! Você ganhou em {cont} tentativas!')
    break
  elif escolha == 'i' and resultado % 2 != 0:
    print(f'Ahhhh droga! Você ganhou em {cont} tentativas!')
    break
  else:
    print('Ganhei! Sou demais mesmo!\nTente novamente!')