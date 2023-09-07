# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('vamos ver se esse triângulo é possível?')
print('_'*50)
r1 = float(input('digite aqui o comprimeiro da primeira reta: '))
r2 = float(input('digite aqui o comprimento da segunda reta: '))
r3 = float(input('por fim, digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('esse triângulo é possivel!')

else:
    print('esse triângulo não pode existir..')