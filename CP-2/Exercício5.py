'''
5. Um investidor aplica um valor inicial (ex: R$ 1000.00) com uma taxa de
juros mensal (ex: 1%). Desenvolva um programa que solicite o valor
inicial, a taxa e a quantidade de meses. O programa deve usar um laço
de repetição para calcular e exibir o saldo mês a mês. (2 pontos)
'''

valor_invest = float(input("Digite o valor inicial para investimento R$: "))
taxa = float(input("Digite o valor da taxe de juros (%): "))
meses = int (input("Digite a quantidade de meses: "))

for i in range (1, meses+1):
    # valor_invest = valor_invest + (valor_invest * (taxa/100))
    valor_invest += valor_invest * (taxa/100)
    print(f"Mês {i}: R$ {valor_invest:.2f}")