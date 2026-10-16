'''
EXERCÍCIO 3
Crie um Algoritmo que solicita a entrada de dois valores
inteiros. O primeiro valor é das "horas" e o segundo dos
"minutos". Valide se a hora e minutos estão dentro do valor
permitido, sendo de 0 até 23 para horas e 0 até 59 para
minutos.
'''

horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))

if horas <= 23 and minutos <= 59:
    print(f'São exatamente: {horas} horas e {minutos} minutos)')
else:
    print('Valor invalido.')
