# exercício 042 - Analisando Triângulos
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 <seg1 + seg2:
  print('Os segmentos acima PODEM formar um triângulo.')

  if seg1 == seg2 == seg3:
    print('O triângulo é equilátero.')
  elif seg1 != seg2 != seg3 != seg1:
    print('O triêngulo é escaleno.')
  else:
    print('O triângulo é isósceles.')

else:
  print('Os segmentos acima NÃO PODEM formar triângulo')