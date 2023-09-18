"""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
A) quantas pessoas tem mais de 18 anos. 
B) quantos homens foram cadastrados. 
C) quantas mulheres tem menos de 20 anos.
"""
#cadastro
print('Cadastre uma pessoa')
cont_idade = 0
cont_masc = 0
cont_fem = 0
while True:
  idade = int(input('Insira a idade: '))
  sexo = str(input('Insira o sexo [M/F]: ')).strip().lower()[0]
  continuar_cadastro = str(input('Deseja continuar?[S/N] ')).strip().lower()[0]

  if sexo == 'm':
    cont_masc += 1
  elif sexo == 'f' and idade < 20:
    cont_fem += 1

  if idade > 18:
    cont_idade += 1

  if continuar_cadastro != 's':
    break

print(f'Você cadastrou {cont_idade} pessoas com mais de 18 anos, {cont_masc} homens e {cont_fem} mulheres com menos de 20 anos.')