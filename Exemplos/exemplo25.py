# DO while
while True:
    n = int(input('Digite 0 ou 1 para sair: '))

    if n == 0 or n == 1:
        print(f'Voce digitou {n} . Saindo do laço')
        break

    print('Voce digitou', n, 'tente novamente!' )

print('Fora do laço!')
