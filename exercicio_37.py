# exercício 037 - Conversor de Bases Numéricas
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opc = int(input('Insira a sua opção: '))

if opc == 1:
  print(f'{num} convertido para BINÁRIO é igual a {num:b}')
elif opc == 2:
  print(f'{num} convertido para OCTAL é igual a {num:o}')
elif opc == 3:
  print(f'{num} convertido para HEXADECIMAL é igual a {num:x}')
else:
  print('Opção inválida, tente novamente.')