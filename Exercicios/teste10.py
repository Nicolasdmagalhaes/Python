# 10. Crie um algoritmo que receba um número inteiro qualquer e exiba a sua
# tabuada de multiplicação do 1 ao 10, apresentando os resultados no
# formato: N x i = Resultado.

x = int(input('Digite um numero: '))

for t in range(1, 11):
    print(f'{x} x {t} = {(t * x)}')


