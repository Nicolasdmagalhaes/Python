# 8. Elabore um algoritmo que receba 15 números inteiros e, ao final, informe
# quantos desses valores estão compreendidos no intervalo entre 10 e 50
# (inclusive).

dentro = 0
fora = 0

for n in range(1,16):
    numero = int(input(f"Digite um número:  "))
    if numero >= 10 and numero <= 50:
        dentro += 1
    else:
        fora += 1
print(f'os numeros no intervalo de 10 a 50 são: {dentro}, e os numeros fora são: {fora}')
