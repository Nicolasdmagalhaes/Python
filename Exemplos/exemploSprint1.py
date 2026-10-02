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

    # Função isdigit(): utilizada para verificar se contém apenas numeros
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            print('Cadastrando o aluno')
            #nome = input('Digite o nome do aluno: ')
        elif opcao == 2:
            print('Consultando o aluno')
        elif opcao == 3:
            print('Atualizando o aluno')
        elif opcao == 4:
            print('Remover o aluno')
        elif opcao == 5:
            print('Listar os alunos ')
        elif opcao == 6:
            print('Saindo do programa')
            break #break só fica na condição de saida
        else:
            print('Voce digitou uma opcao invalida. Tente novamente')
    else:
        print('Digite apenas numeros. De 0 até 6')