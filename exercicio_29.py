# exercicio 29 - Radar Eletrônico

velocidade = float(input('Escreva aqui a velocidade do veículo: '))
multa = (velocidade-80)*7

if velocidade > 80:
    print(f'Correu demais e foi multado! Sua multa é de {multa}R$')
else:
    print('Parabéns, se manteu na velocidade permitida (:')