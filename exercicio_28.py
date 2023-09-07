# exercicio 28 - Jogo de adivinhação

import random
from time import sleep
print('Vamos ver se você consegue descobrir o número de 0 a 5 que estou pensando,')
computador = (random.randrange(0,5))
escolhido = int(input('Digite aqui o seu palpite: '))
print('PROCESSANDO...')
sleep(3)
print('-=-'*25)
if escolhido == computador:
    print(f'Parabéns! O número que o computador pensou foi {escolhido} e você acertou')
else:
    print(f'Errrrrrrouuuuu, o número que o computador escolheu foi {computador}')