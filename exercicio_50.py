"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o."""

cont = 0
soma = 0
for n in range(1,7):
  n = int(input(f'Digite o {n}⁰ valor: '))

  if n % 2 == 0:
    cont += 1
    soma += n
print(f'existem {cont} números pares que juntos somam {soma}.')