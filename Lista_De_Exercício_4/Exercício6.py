'''
6. Elabore um algoritmo que leia 10 números inteiros e identifique o menor
valor entre eles, exibindo-o ao final da execução.
'''
menor = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))

    if i == 0:
        menor = num
    elif num < menor:
        menor = num

print("O menor valor é:", menor)



