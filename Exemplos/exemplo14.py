idade = int(input('Digite a sua idade: '))

match idade:
# X é o valor que vvem da variavel (idade)
# Foi definido uma variavel genérica para informar um valor possivel
    case x if x >= 18:
        print('Maior de idade')
    case x if x < 18:
        print('Menor de idade')
    case _:
        print('Valor invalido')