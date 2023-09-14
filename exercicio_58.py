"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random
print('Sou o seu computador e vou propor um desafio!\nVou pensar em um número de 0 a 10, você consegue advinhar qual é?')
palpite = int(input('Qual é o seu palpite? '))
tentativas = 0
n = random.randrange(1,10)
while palpite != n:
  palpite = int(input('Errrrouuuuuuu! tente mais uma vez! '))
  tentativas += 1

print(f'Parabéns! Você acertou em {tentativas} tentativas!')

