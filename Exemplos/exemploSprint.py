# Gerencia Aluno
# 1 - Cadastrar
# 2 - Consultar
# 3 - Atualizar
# 4 - Remover
# 5 - Listar Alunos
# 6 - Sair do programa

while True:
    print('Gerenciar Aluno')
    print('1 - Cadastrar')
    print('2 - Consultar')
    print('3 - Atualizar')
    print('4 - Remover')
    print('5 - Listar')
    print('6 - Sair')
    opcao = input('Digite uma opcao: ')
# Do 1 até o 5 ira repetir por conta do break no 6
# Função isdigit(): utilizada para verificar se contém apenas numeros
    if opcao.isdigit():
        opcao = int(opcao)
        match opcao:
            case 1:
                print('Cadastrando o aluno')
            #nome = input('Digite o nome do aluno: ')
            case 2:
                print('Consultando o aluno')
            case 3:
                print('Atualizando o aluno')
            case 4:
                print('Remover o aluno')
            case 5:
                print('Listar os alunos ')
            case 6:
                print('Saindo do programa')
                break #break só fica na condição de saida
            case _:
                print('Voce digitou uma opcao invalida. Tente novamente')

    else:
        print('Digite apenas numeros. De 0 até 6')