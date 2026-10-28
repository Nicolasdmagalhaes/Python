'''
1. Exemplo de função com return, uma função não permite +1 de um Retorno
'''

def calcular_media(n1, n2):  # Os Parametros de entrada não é obrigatorio
    return (n1 + n2) / 2 # O return é opcional

# 2. Posso guarda esse retorno dentro de uma variavel
media = calcular_media(10, 5)
print(media)

# 3. Chamando a função dentro do print
print(calcular_media(6, 20))