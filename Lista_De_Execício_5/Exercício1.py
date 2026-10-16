'''
1. Crie um Algoritmo que o nome de um dia da semana (ex: "Sábado",
"Segunda"). Usando match-case, o programa deve informar se é um
"Dia útil" ou "Final de semana".
'''

dia = (input('Digite o dia da semana: ')).lower()

match dia:
    case "domingo" | "sábado":
        print('Final de semana!')
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print('Dia útil!')
    case _:
        print('Dia invalido!')
