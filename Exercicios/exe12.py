horas = int(input('horas:'))
minutos = int(input('minutos:'))

if horas >= 0 and horas <=23 and minutos >= 0 and minutos <= 59:
    print(f'são extamente: {horas} horas e {minutos} minutos ')
else:
    print('valor invalido')
