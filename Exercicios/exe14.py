n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 == n2 == n3:
    print('Esses numeros são iguais')
elif n1<n2 and n1<n3:
    print(f'Esse é o menor número: {n1}')
elif n2 <n1 and n2<n3:
    print(f'Esse é o menor número: {n2}')
else:
    print(f'esse é o menor numero: {n3}')