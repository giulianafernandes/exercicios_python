# exercicio 30 - Par ou Ímpar

numero = int(input('Digite aqui um número inteiro: '))
par = numero % 2

if par==0:
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')