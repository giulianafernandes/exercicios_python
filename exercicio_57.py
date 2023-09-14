"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Qual é o seu sexo(M/F)? ')).strip().upper()[0]
while sexo not in 'MF':
   sexo = str(input('O valor digitado está incorreto, insira novamente(M/F): ')).strip().upper()[0]
print('Registrado com sucesso.')