# 1. Utilizando uma função para alterar o valor da variavel global

x = 0
def alterar(n1):
#     x = n1 # Redeclarando
#    global x # Substituindo o valor de x
     x = n1
     print(x)

alterar(7)
print(x)

''' 
2. A variavel não pode ser substituida de qualquer jeito!,
(se não chamar a função), Global substitui o valor da variavel que está por fora.
'''
