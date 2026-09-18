idade = int(input('Digite a sua idade: '))
cnh = input('Tem CNH? (sim ou não)? ').lower()

match idade,cnh:
# i idade c cnh
    case i,c, if i>=18 and c=='sim':
        print('Permitido dirigir!')
    case i,c if i<18 and c=='não':
        print('Não é permitido dirigir!')
    case i,c if i>= 18 and c=='não':
        print('Tem cnh mas não pode dirigir!')
    case _:
        print('Valores invalidos!')

# Ou
match idade,cnh:
    case i, _ if i < 0:
        print('idade invalida!')
    case i, 'sim' if i>= 18 :
        print('Permitido dirigir!')
    case i, 'não' if i<18 :
        print('Não é permitido dirigir!')
    case i, 'não' if i>= 18 :
        print('Tem cnh mas não pode dirigir!')
    case i, 'sim' if i<18 :
        print('Voce não tem idade para tirar CNH, mas não pode dirigir!')
    case _:
        print('Valores invalidos!')
