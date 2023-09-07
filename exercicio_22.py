# Crie um programa que leia o nome completo de uma pessoa.

nome=str(input('Olá! Digite o seu nome completo: ')).strip()

# nome com todas as letras maiúsculas
print(f'Seu nome em maiúsculas é {nome.upper()}')

# com todas as letras minúsculas
print(f'Seu nome em minúsculas é {nome.lower()}')

# quantas letras tem ao todo sem considerar os espaços
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')

# quantas letras tem o primeiro nome
primeironome = nome.split()
print(f'Seu primeiro nome tem {len(primeironome[0])} letras')