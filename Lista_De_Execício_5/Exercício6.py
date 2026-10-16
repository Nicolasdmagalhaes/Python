'''Crie um Algoritmo para um restaurante realizar o fechamento de
comandas.
a. Deve solicitar o código do prato.
 ---CÓDIGO---
 1 Hamburguer -------- R$ 40,00
 2 Lasanha --------- R$ 60,00
 3 Bife acebolado ------- R$ 30,00
 4 Strogonoff ---------- R$ 35,00
 5 Picanha------------ R$ 60,00
 6 Churrasco -------------R$ 60,00
b. Em seguida, deve perguntar se o cliente deseja incluir a taxa de
serviço de 10% (Sim ou Não).
c. Calcule o valor final:
i. Se aceitar a taxa: Total} = Preço* 1.10$
ii. Se não aceitar: Total=Preço
d. Exiba o nome do prato escolhido e o valor total a pagar. Caso o
código seja inexistente, informe "Prato não encontrado".'''

print('Comandas')
codigo = input('Digite o código do prato (1 a 6): ')

match codigo:
    case '1':
        prato, preco = 'Hamburguer', 40.00
    case '2':
        prato, preco = 'Lasanha', 60.00
    case '3':
        prato, preco = 'Bife acebolado', 30.00
    case '4':
        prato, preco = 'Strogonoff', 35.00
    case '5':
        prato, preco = 'Picanha', 60.00
    case '6':
        prato, preco = 'Churrasco', 60.00
    case _:
        prato, preco = None, 0

match prato:
    case None:
        print('Prato não encontrado')
    case _:
        taxa = input('Deseja incluir a taxa de serviço de 10%? (Sim ou Não): ').lower()

        match taxa:
            case 'sim' | 's':
                total = preco * 1.10
                print(f'Prato: {prato}')
                print(f'Total a pagar: R$ {total:.2f}')
            case 'não' | 'nao' | 'n':
                total = preco
                print(f'Prato: {prato}')
                print(f'Total a pagar: R$ {total:.2f}')
            case _:
                print('Resposta inválida! Digite Sim ou Não.')