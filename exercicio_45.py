#exercício 045 - GAME: Pedra, papel e Tesoura

import random

print ('=-*-'*15)
print ('JOKEEEEEENPÔ!')

pessoa = str(input('hora de escolher! PEDRA, PAPEL OU TESOURA?')).strip()
pc = ['pedra','papel', 'tesoura']
escolhapc = (random.choice(pc))

if pessoa == 'tesoura' and escolhapc == 'pedra':
    print('muaaaaahahahaha! perdeu! escolhi pedra!')
elif pessoa == 'tesoura' and escolhapc == 'papel':
    print(f'O que? {pessoa}? eu perdi? escolhi {escolhapc}, não acredito!')
elif pessoa == 'tesoura'and escolhapc == 'tesoura':
    print ('EMPATE!')

elif pessoa == 'papel' and escolhapc == 'tesoura':
    print(f'EU GANHEI! {escolhapc} corta papel! ')
elif pessoa == 'papel' and escolhapc == 'pedra':
    print(f'escolhi {escolhapc} e perdi! :( você está ficando melhor nisso!')
elif pessoa == 'papel' and escolhapc == 'papel':
    print('IMPATE!')

elif pessoa == 'pedra' and escolhapc == 'papel':
    print('EU SOU INVENCÍVEL! papel enrola a pedra, muahahahahaha!')
elif pessoa == 'pedra' and escolhapc == 'tesoura':
    print(f'ganhou de novo? aaaaaah não! escolhi {escolhapc}')
elif pessoa == 'pedra' and escolhapc == 'pedra':
    print('EMPATE!')