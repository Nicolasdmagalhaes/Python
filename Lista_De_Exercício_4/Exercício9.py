'''
Desenvolva um algoritmo que solicite o salário atual de um funcionário e
o percentual de reajuste. O programa deve calcular o valor do aumento
e exibir o novo salário atualizado.
'''

salario_atual = int(input('Digite o salario atual do funcionario:  '))
reajuste = int(input('Digite o reajuste do funcionario: '))

reajuste = (reajuste / 100)

# salario_ajustado = ((reajuste / 100) * salario_atual) + salario_atual | Existe uma maneira de fazer direto também


print('O salário atual do funcionario é de r$:', salario_atual + (salario_atual * reajuste))



