a = int(input('Informe os dias para a atividade A: '))
b = int(input('Informe os dias para a atividade B: '))
c = int(input('Informe os dias para a atividade C: '))

if (a >= 0 and b >= 0 and c >= 0):
    tempo_total =(a+b+c)
    print(f'Tempo total é de {tempo_total} dias.')
else:
    print('Erro: Os dias não podem ser negativos.')
