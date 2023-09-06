# exercício 039 - Alistamento Militar
from datetime import date
sexo = str(input('Digite aqui o seu sexo biológico: ')).strip().lower()
idade = date.today().year - ano_nasc

if sexo == 'feminino':
  print('Você não precisa se apresentar ao exército.')

elif sexo == 'masculino':
  ano_nasc = int(input('Digite o ano do seu nascimento: '))

  if idade == 18:
    print('Você fez 18 anos, está na hora exata de se alistar.')
  elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
    print(f'Seu alistamento será em {date.today().year + (18 - idade)}.')
  elif idade > 18:
    print(f'Você já passou da idade de alistamento {idade - 18} anos')
    print(f'Seu alistamento foi em {date.today().year - (idade - 18)}.')

else:
  print('Sexo inválido.')
