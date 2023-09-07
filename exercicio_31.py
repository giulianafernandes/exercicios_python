#exercício 31 - Custo da Viagem

distancia = float(input('Olá! Escreva aqui quantos km você vai percorrer:'))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f'A sua passagem custará {preço}R$')