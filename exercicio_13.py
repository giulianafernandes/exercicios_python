# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

# sa = salário atual
sa = float(input('Digite aqui o seu salário atual: '))

# au = aumento de salário
au = sa + (sa*15/100)

print('Parabéns, você ganhou um aumento de 15%! Seu novo salário é de {:.2f}R$!'.format(au))
