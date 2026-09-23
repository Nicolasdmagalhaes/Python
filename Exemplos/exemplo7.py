senha =  input('Digite a senha: ')
usuario = input('Digite o nome do usuario:')

if senha != 'Fiap' or usuario !='Admin':
    print('Senha ou usuario incorreta')
else:
    print('Acesso permitido!')

# O or pro and muda completamente a logica do dado

if senha != 'Fiap' and usuario !='Admin':
    print('Acesso permitido')
else:
    print('Senha incorreta!')


