horas = int(input('Horas:'))
minutos = int(input('Minutos:'))

if horas >= 0 and horas <=23 and minutos >= 0 and minutos <= 59:
    print(f'São extamente: {horas} horas e {minutos} minutos ')
else:
    print('valor invalido')
