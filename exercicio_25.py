# Crie um programa que verifique se existe a palavra Silva no nome de uma pessoa

nome = str(input('Qual é o seu nome completo? ')).strip()

print(f'Seu nome tem Silva? {"silva" in nome.lower()}')