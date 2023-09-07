# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente desse ângulo.

import math

#angulo
an=float(input('Digite aqui o ângulo que você deseja: '))


seno=math.sin(math.radians(an))
coseno=math.cos(math.radians(an))
tangente=math.tan(math.radians(an))

print('O valor do seno é {:.2}, do coseno é {:.2} e da tangente é {:.2}!'.format(seno, coseno, tangente))

