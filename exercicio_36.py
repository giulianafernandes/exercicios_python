# exercício 036 - Aprovando Empréstimo

valor_casa = float(input('Olá! Insira o valor do imóvel: R$'))
salario = float(input('Insira o seu salário: R$'))
anos = int(input('Em quantos anos pretente pagar o imóvel: '))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal > 0.3 * salario:
  print('Emprestimo negado. O valor da prestação ultrapassa 30% do seu salário.')

else:
  print('Emprestimo aprovado!')

print(f'Para pagar uma casa de R${valor_casa} em {anos} anos, a prestação será de R${prestacao_mensal}')