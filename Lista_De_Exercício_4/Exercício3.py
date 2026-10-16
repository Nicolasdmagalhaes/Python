'''
3. Escreva um algoritmo que leia números indeterminados até que o valor,
 zero seja inserido. Ao encerrar, apresente a soma de todos os valores digitados.
'''

soma = 0 # A variavel soma aumenta a cada numero novo digitado
numero = int(input("Digite um número (0 para encerrar): ")) # o número séra a variavel que armazenara os numeros

while numero != 0: # aqui qualquer número diferente de 0 volta a repetição
    soma += numero # o soma += numero armazena cada numero
    numero = int(input("Digite um número (0 para encerrar): ")) # coloco ele denovo para entrar no loop

print("A soma dos valores digitados é:", soma) #não precisa colocar dentro do { }

