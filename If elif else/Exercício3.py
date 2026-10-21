limite = 3000

dispesas = int(input('Digite o total de despesas do mês: '))

if dispesas > limite:
    print('Atenção! Vooce ultrapassou o limite do orçamento.')
else:
    print('Voce está dentro do orçamento')