"""
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
continuar = 's'
soma = 0
cont = 0
maior = 0
menor = 0
while continuar == 's':
  n = int(input('Digite um número inteiro: '))
  continuar = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
  soma += n
  cont += 1
  if cont == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
media = soma / cont
print(f'Você digitou {cont} números, a média dos valores foi de {media}\nO maior número foi {maior} e o menor {menor}.')
