# Escreva um algoritmo que receba um número inteiro positivo N e calcule
# o seu fatorial. Lembre-se que o fatorial é o produto de todos os inteiros
# positivos menores ou iguais a N.

n = int(input("Digite um número inteiro positivo: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial = fatorial * i

print("O fatorial é:", fatorial)