#exercicio 04 - Dissecando uma variável

x = input('Digite algo:')
print(x, 'É do tipo primitivo:',type(x))
print(x, 'É Alphanumérico?', x.isalnum())
print(x, 'Tem letras?', x.isalpha())
print(x, 'Tem números?', x.isnumeric())
print(x, 'Está escrito em letras maiúsculas?', x.isupper())
print(x, 'Está escrito em letras minúsculas?', x.islower())
print(x, 'Posso imprimir?', x.isprintable())
