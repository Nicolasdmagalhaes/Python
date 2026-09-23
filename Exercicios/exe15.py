salf = int(input('Salário fixo: '))
vlvendas = int(input('Valor das vendas: '))
cbase = int()
cextra = int()

if vlvendas <= 5000:
    cbase = 5000 * 0.05
else:
    cextra = (vlvendas - 5000) * 0.07
    cbase = 5000 * 0.05

soma = cbase + cextra
saltotal = (salf + soma)

print(f'Com um total de comissão de R$: {soma} nesse mes, o salario final seria R$: {saltotal}')


