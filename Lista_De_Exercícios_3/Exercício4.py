'''
EXERCÍCIO 4
Crie um Algoritmo que solicita a entrada de dois valores
inteiros e exiba apenas o maior entre eles. Caso sejam
iguais, exiba a mensagem "Números iguais".
'''

maior = int(input('Digite um número: '))
menor = int(input('Digite o segundo número: '))

if maior == menor:
    print('Números iguais!')
elif maior > menor:
    print(f'O maior número é o {maior}!')
else:
    print(f'O maior número é o {menor}!')

