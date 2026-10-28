nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

media = (nota1 + nota2) / 2
if media >= 5:
    print(f'Média {media} - Aprovado')
else:
    print(f'Média {media} - Reprovado')