# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o compriento da hipotenusa.
import math

#cateto oposto
co=float(input('Digite aqui o comprimento do cateto oposto: '))

#cateto adjacente
ca=float(input('Digite agora o comprimento do cateto adjacente: '))

# hipotenusa calculada usando o módulo math
hipotenusa=math.hypot(co,ca)

print(f'O comprimento da hipotenusa é {hipotenusa}')