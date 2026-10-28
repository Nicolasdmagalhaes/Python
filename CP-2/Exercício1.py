'''
1. Crie um programa que solicite ao usuário uma nota entre 0 e 10. O
programa deve continuar pedindo a nota enquanto o valor digitado for
inválido (fora da faixa). Quando um valor válido for inserido, exiba: "Nota
[valor] registrada com sucesso" (1 ponto)

Digite uma Nota [0 até 10]: 10
Nota “10” registrada com sucesso

Digite uma Nota: 11
Nota inválida. É apenas aceito de 0 até 10
Digite uma Nota:
'''
while True:
    nota = float(input("Digite uma nota [0 até 10]: "))

    while nota<=0 or nota>=10:
        print("Nota inválida. É apenas aceito de 0 até 10.")
        nota = float(input("Digite uma nota [0 até 10]: "))

    print(f"Nota {nota} registrada com sucesso")
    break

# podemos fazer desses 2 modos

while True:
    nota = float(input("Digite uma nota [0 até 10]: "))

    if nota >= 0 and nota <= 10:
        print(f"Nota {nota} registrada com sucesso")
        break
    else:
        print("Nota inválida. É apenas aceito de 0 até 10.")