"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

media_idade = 0
sexo_fem = 0
idade_maisvelho = 0
nome_maisvelho = 0
for pessoa in range (1,5):
  nome = str(input(f'Digite o nome da {pessoa}a pessoa: '))
  idade = int(input('Idade: '))
  media_idade += idade
  sexo = str(input('Sexo (M/F): ')).upper().strip()
  if sexo == 'M' and pessoa == 1:
    idade_maisvelho = idade
    nome_maisvelho = nome
  if sexo == 'M' and idade > idade_maisvelho:
    idade_maisvelho = idade
    nome_maisvelho = nome
  if idade <= 20 and sexo == 'F':
    sexo_fem += 1
print(f'A média de idade do grupo é de {media_idade/4} anos.')
print(f'O homem mais velho do grupo é o {nome_maisvelho} e ele tem {idade_maisvelho} anos.')
print(f'O grupo tem {sexo_fem} mulheres com menos de 20 anos.')