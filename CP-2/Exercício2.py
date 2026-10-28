'''
2. Desenvolva um algoritmo que peça um número inteiro ao usuário e
exiba a tabuada desse número de 1 a 10 no formato: X * 1 = X. (1
ponto)
'''

while True:
    numero = int(input("Digite um número [1 até 10]: "))

    if numero>= 1 and numero<=10:
        break
    else:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")

    # I: incremento (é o contador)
for i in range(1,11): #(start, stop) (1 até 10) <= <
    print(f"{numero} x {i} = {numero * i}")