# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária paara pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2.

l = float(input('Digite aqui a largura da sua parede em metros: '))
a = float(input('Digite aqui a altura da sua parede em metros: '))

m2 = a*l
t = (a*l)/2

print('Você vai precisar de {} litros de tinta'.format(t))
