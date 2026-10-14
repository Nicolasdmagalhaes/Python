'''EXERCÍCIO 6
Crie um algoritmo que calcula o salário de um determinado
vendedor. É necessário solicitar a entrada:
 a. Salário Fixo
 b. Valor de Vendas
Sabendo-se que ele recebe uma comissão de 5% sobre o total
das vendas em até R$5.000,00 e 7% sobre o que ultrapassar.
Exiba o salário total do vendedor e a comissão que ele irá
receber.'''

salfixo = float(input('Digite seu salário: '))
valvendas = float(input('Valor de vendas: '))

if valvendas <= 5000:
    comissao = valvendas * 0.05
else:
    comissao = 5000 * 0.05 + (valvendas - 5000) * 0.07

saltotal = salfixo + comissao


print(f'O salário total do vendedor foi de {saltotal:.2f} e sua comissao foi de {comissao:.2f}')
