# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n1 = int(input('Digite um número: '))
db = n1 * 2
tp = n1 * 3
rz = n1 ** (1/2)

print ('O dobro de {} é {}, o triplo é {} e a sua raiz quadrada é {}'.format(n1, db, tp, rz))