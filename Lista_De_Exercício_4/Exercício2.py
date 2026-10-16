'''
2. Elabore um algoritmo que receba a idade de 10 pessoas e, ao final, exiba o total de passeoas menores de 18 anos.'
'''

menores = 0 # Variavel que o exercicio pede que seriam os menores de 18 anos

for p in range(1, 11): # Aqui o P vai ser a quantidade de pessoas
    idade = int(input(f"Digite a idade da pessoa {p}: ")) # Aqui eu faço  a variavel idade

    if idade <= 17: # Esse if seria para validar os maiores de 18
        menores += 1 # aqui almentaria o número

print(f'Total de pessoas menores de 18 anos: {menores}')
