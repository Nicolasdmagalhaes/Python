# 5. Desenvolva um algoritmo que receba dois números distintos. Utilize uma
# estrutura de repetição para garantir que os valores sejam diferentes e,
# após a validação, exiba a soma entre eles.

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

while True :
    if a != b:
        soma = a + b
        print('A Soma dos números diferentes são:', soma)
        break
    else:
        a == b
        print('Valores iguais não pode!')
        break