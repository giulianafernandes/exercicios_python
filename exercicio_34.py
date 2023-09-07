# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Escreva aqui o seu salário: '))

maisaltos = salario*10/100
maisbaixos = salario*15/100

if salario > 1250:
    print(f"Você ganhava {salario:.2f}R$, com o aumento de 10% seu salário fica {salario + maisaltos}R$"
    )

else:
    print(f'Você ganhava {salario:.2f}R$, com o aumento de 15% seu salário fica {salario+maisbaixos}R$')