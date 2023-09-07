# Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit

celcius = float(input('Digite aqui a temperatura de onde você está: '))

fahrenheit = (celcius*1.8)+32
print('A temperatura de {}°C corresponde a {}°F'.format(celcius, fahrenheit))
