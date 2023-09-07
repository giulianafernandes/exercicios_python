# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = int(input('Adicione aqui a metragem a ser convertida: '))
cm = n1 * 100
mm = n1 * 1000


print ('{} metros tem {} centímetos e {} milímetros'.format(n1, cm, mm))