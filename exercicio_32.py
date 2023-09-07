# exercicio 32 - Ano Bissexto 

from datetime import date
ano = int(input('Escreva o ano que você quer analisar. Para Analisar o ano atual digite 0.'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto e o mês de fevereiro tem 29 dias (:')
else:
    print(f'O ano {ano} não é Bissexto e continua tento 365 dias!')