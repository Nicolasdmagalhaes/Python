idade = int(input('Digite sua idade: '))
cnh = input('Tem CNH? ( sim ou não): ')

if idade >= 18 and cnh =='sim':
    print('Você é permitido a dirigir')
elif idade >=18 and cnh == 'não':
    print('Você tem o direito de tirar a sua cnh, mas não pode dirigir')
else:
    print('Você não pode dirigir')

# Não usando operador logico

if idade>=18:
    if cnh == 'sim':
        print("Você é permitido a dirigir")
    else:
        print('Você tem o direito de tirar a sua cnh, mas não pode dirigir')
else:
    print('Você não pode dirigir')