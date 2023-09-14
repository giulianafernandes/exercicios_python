# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# minha resposta
frase = str(input('Digite uma frase: ')).lower().strip()
frase = frase.replace(' ','')
inversao = ''.join(reversed(frase))

print(f'A {frase} invertida é {inversao} :D')

if frase == inversao:
  print('Esta frase é um palíndromo')
else:
  print('Esta frase não é um palíndromo!')


# resposta do professor
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
  print('Temos um palíndromo!')
else:
  print('A frase não é um palíndromo!')