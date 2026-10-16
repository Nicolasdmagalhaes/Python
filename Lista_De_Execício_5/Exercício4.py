'''
4. Crie um Algoritmo que recebe um número inteiro e mostre o menu para
selecionar o tipo de cálculo que deve ser realizado. Exiba o resultado do
cálculo efetuado.
1 - O dobro
2 - A metade
3 - 10% do número.
'''

valor = int(input('Digite um número inteiro: '))
menu = int(input('Escolha uma opção: ''1 - O dobro , 2 - A metade , 3 - 10% do número: '))

match menu:
    case 1:
        print(f'O dobro do valor escolhido é: {valor*2}')
    case 2:
        print(f'A metade do valor é: {valor/2}')
    case 3:
        print(f'10% do valor escolhido é: {valor*0.10}')
    case _:
        print('Opção invalida')


