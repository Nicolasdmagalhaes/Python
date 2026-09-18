opcao = int(input('Digite sua opcao (0 até 3): '))
# Estrutura do match-case por padrão compara valores por igualdade
# No match não há limitação para case, podemos ter
# Porém de maneira mínima há 1 case e 1 case default (case _:)

match opcao:
# Possivel menu
    case 0:
        print('Opção 0')
    case 1:
        print('Opção 1')
    case 2:
        print('Opção 2')
    case 3:
        print('Opção 3')
    case _:
        print('Valor invalido. DIgite de 0 até 3')

# Podemos usar o if e o elif, else

if opcao == 0:
    print('Opção 0')
elif opcao == 1:
    print('Opção')
elif opcao == 2:
    print('Opção 2')
elif opcao == 3:
    print('Opção 3')
else:
    print('Valor invalido. DIgite de 0 até 3')
