"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
maiores = 0
menores = 0
for c in range(1,8):
  ano = int(input(f'Em que ano a pessoa {c}ª nasceu? '))
  if date.today().year - ano >= 18:
      maiores += 1
  else:
      menores += 1
print(f'Neste grupo tem {maiores} pessoas maiores de idade e {menores} pessoas menores de idade.')