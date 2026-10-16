'''
4. Crie um algoritmo que solicite ao usuário a quantidade N de valores a
serem lidos. Em seguida, calcule e exiba separadamente a média
aritmética dos números pares e a média dos números ímpares
informados.
'''

# Aqui seria as variaveis sem print
soma = 0
par = 0
impar = 0
qtd_impar = 0 # isso aqui seria os numeros par
qtd_par = 0 # isso aqui seria os numeros impar

while True:
    n = int(input("Digite um número: ")) # colocariamos aqui o (n = int) pra ele entrar no while criar o laço de repetição
    if n == 0: # esse == 0 seria o numero para parar o programa
        break
    elif n % 2 == 0:   # se for par ele acrescenta o numero digitado pelo teclado
        qtd_par += 1
        par += n
    else:
        qtd_impar += 1
        impar += n

if qtd_par > 0:
    print("A média de pares: ", (par / qtd_par))

if qtd_impar > 0: # aqui ele vai validar os numeros que não podem dividir por zero
    print("A média de impares: ", (impar/qtd_impar))






