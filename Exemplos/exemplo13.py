dia = (input('Digite o dia da Semana: ')).lower()
# Função lower: transformar texto em minusculo
# Or no match é o ( | ) pipe
# Não é possivel usar a palavra OR
match dia:
    case 'segunda' | 'terça' | 'quarta' | 'quinta'| 'sexta':
        print('Dia útil')
    case 'sabado' | 'domingo':
        print('Final de Semana')
    case _:
        print('Dia Invalido')

# Podemos fazer com if, elif, else!
if dia == 'segunda' or dia== 'terça' or dia== 'quarta' or dia== 'quinta' or dia== 'sexta':
    print('Dia útil')
elif dia == 'sabado' or dia == 'domingo':
    print('Final de semana')
else:
    print('Dia Invalido')

# Podemos fazer cortanddo linha!
if (dia == 'segunda'
    or dia == 'terça'
    or dia == 'quarta'
    or dia == 'quinta'
    or dia == 'sexta'):
    print('Dia útil')
elif dia == 'sabado' or dia == 'domingo':
    print('Final de semana')
else:
    print('Dia Invalido')


