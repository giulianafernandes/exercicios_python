# exercício 041 - Classificando Atletas
from datetime import date

ano = int(input('Digite aqui o seu ano de nascimento: '))
idade = date.today().year - ano

print(f'O aluno tem {idade} anos')

if idade <= 9:
  print('A categoria dele é MIRIM.')
elif idade <= 14:
  print('A categoria dele é INFANTIL')
elif idade <= 19:
  print('A categoria dele é JÚNIOR')
elif idade <= 25:
  print('A categoria dele é SÊNIOR')
else:
  print('A categoria dele é MASTER')