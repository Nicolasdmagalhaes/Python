'''
5. Crie um Algoritmo para um recepcionista realizar operações rápidas no
sistema de reservas, com as seguintes opções:
1. Check-in
2. Check-out
3. Consultar Quarto
4. Sair
'''

print('SISTEMA DE RESERVAS')
print('1. Check-in')
print('2. Check-out')
print('3. Consultar Quarto')
print('4. Sair')

opcao = int(input('Esolha uma opção: '))
match opcao:
    case 1:
        print(f'Seu check-in foi realizado com sucesso!')
    case 2:
        print(f'Seu check-out foi realizado com sucesso!')
    case 3:
        print(f'Quarto disponivel!')
    case 4:
        print(f'Saindo do sistema!')
    case _:
        print('Opção invalida')


