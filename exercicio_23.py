# Faça um programa que leia na tela um número de 0 a 9999 e mostre cada um dos dígitos separados.

num=int(input('Escreva um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#unidade
print('A unidade é:')
print(u)

#dezena
print('A dezena é:')
print(d)

#centena
print('A centena é:')
print(c)

#milhar
print('O milhar é:')
print(m)
