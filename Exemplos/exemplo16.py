idade = int(input('Digite a sua idade: '))
cnh = input('Tem CNH? (sim ou não)? ').lower()

if idade<=0:
    print('Idade Invalido!')
elif idade>=18 and cnh=='sim':
    print('Permitido a dirigir')
elif idade>=18 and cnh=='não':
    print('Tem idade para dirigir, mas voce não uma tem cnh')
elif idade<18 and cnh=='não':
    print('Não é permitidod dirigir')
elif idade<18 and cnh=='sim':
    print('Voce não tem idade suficiente para ter uma Cnh!')
else:
    print('Valores invalido')