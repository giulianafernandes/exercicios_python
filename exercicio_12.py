# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Digite aqui o preço do produto: '))
d = p-(p*5/100)


print('O preço do produto com 5% OFF é {:.2f}R$'.format(d))