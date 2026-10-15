# 6. Elabore um algoritmo que leia 10 números inteiros e identifique o menor
# valor entre eles, exibindo-o ao final da execução.

menor = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))

    if i == 0:
        menor = num
    elif num < menor:
        menor = num

print("O menor valor é:", menor)

#menor = 0 → cria a variável que vai guardar o menor número. O valor será substituído pelo primeiro número digitado.
#for i in range(10): → repete o código 10 vezes.
#num = int(input(...)) → pede um número inteiro ao usuário.
#if i == 0: → verifica se é a primeira vez que o código está repetindo.
#menor = num → guarda o primeiro número como o menor.
#elif num < menor: → verifica se o novo número é menor que o anterior menor.
#menor = num → se for menor, guarda o novo número.
#print(...) → mostra o menor número no final.


