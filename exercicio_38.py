# exercício 038 - Comparando números
n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))

if n1 > n2:
  print(f'{n1} é maior que {n2}')
elif n2 > n1:
  print(f'{n2} é maior que {n1}')
elif n1 == n2:
  print('os números são iguais')