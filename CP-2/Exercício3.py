'''
3. Escreva um programa que receba números inteiros positivos do usuário.
O programa deve parar quando o usuário digitar 0. Ao final, o sistema
deve exibir a soma total dos números digitados e a média aritmética
(excluindo o zero da média) (1 ponto)
'''
soma = 0
qtd = 0

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break
    elif numero>0:
        #soma = soma + numero
        soma += numero
        #qtd = qtd + 1
        qtd +=1
    else:
        print("Número inválido")

print(f"Somatória: {soma}")

media = soma / qtd
print(f"Média: {media:.2f}")