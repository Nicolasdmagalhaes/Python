'''
3. Crie um Algoritmo que solicita a entrada do nome de um mês (ex:
"Janeiro", "Julho"). O mesmo deve informar em que estação do ano esse
mês se encontra (considerando o Hemisfério Sul):
• Verão: Dezembro, Janeiro, Fevereiro.
• Outono: Março, Abril, Maio.
• Inverno: Junho, Julho, Agosto.
• Primavera: Setembro, Outubro, Novembro.
'''

mes = input('Digite um més: ').lower()

match mes:
    case 'dezembro'| 'janeiro'| 'fevereiro':
        print('Você está no Verão!')
    case 'março' | 'abril'| 'maio':
        print('Você está no Outono!')
    case 'junho' | 'julho'| 'agosto':
        print('Você está no Inverno!')
    case 'setembro' | 'outubro'| 'novembro':
        print('Você está no Primavera!')
    case _:
        print('ESTA INVALIDO')