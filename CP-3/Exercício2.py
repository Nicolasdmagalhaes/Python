
def tabuada(numero):

    for t in range(1,11):
        resultado = numero*t
        print(f'{numero} x {t} = {resultado}')

def valida_numero():
    while True:
        numero = int(input('Digite um numero [1 até a 10]: '))
        if numero >=1 and numero <=10:
            return numero
        else:
            print('Valor fora do Intervalo! [só pode ser de 1 até a 10]')

def main():
    numero = valida_numero()
    tabuada(numero)

main()

