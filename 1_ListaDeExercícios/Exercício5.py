'''EXERCÍCIO 5
Crie um algoritmo que solicita a entrada de três valores
inteiros e exiba apenas o menor entre eles. Caso sejam
iguais, exiba a mensagem "Números iguais".'''

a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a == b == c:
    print("Números iguais")
elif a <= b and a <= c:
    print(f"O menor é {a}")
elif b <= a and b <= c:
    print(f"O menor é {b}")
else:
    print(f"O menor é {c}")
