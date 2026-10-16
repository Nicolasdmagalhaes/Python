'''
EXERCÍCIO 1
Crie um Algoritmo que solicita a entrada de um valor inteiro
e exiba uma mensagem: "é número par" OU "é número ímpar".
'''

nu = int(input("Digite um número: "))

if nu % 2 == 0:
    print('É número par')
else:
    print('É número impar')