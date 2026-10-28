# 1. Função com variavel local

def alterar(n1):
    x = n1
    print(x)
'''
2. x é uma variavel local, x é desconhecido por todo o código, apenas essa função,
tem conhecimento de x 
'''

'''
3. chamando a variavel local fora da função
[  print(x)  ] ira causar erro de localização de variavel 
(ela não existe)
'''
alterar(10)
