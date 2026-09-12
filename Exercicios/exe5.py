salrario_base = 1800.00
comissao_fixa = 150.00
sobre_vtotal_das_venda =  0.03

nome = input('Nome do vendedor: ')
QPvendidos = int(input('Quantidade produtos vendidos: '))
Vlt = float(input('Valor total das venda: '))

sal = salrario_base +(comissao_fixa*QPvendidos)+ (Vlt*0.03)
print(f'salrio final: R${sal}')
