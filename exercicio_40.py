# exercício 040 - Médias

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
  print(f'Sua média foi de {media}\nREPROVADO')

elif media >= 7.0:
  print(f'Sua média foi de {media}\nAPROVADO!')

elif media >= 5.0 and media <= 7.0:
  print(f'Sua média foi de {media}\nRECUPERAÇÃ0.')