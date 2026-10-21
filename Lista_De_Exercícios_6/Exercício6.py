'''
6. Crie a função maior_numero(a, b), que devolva o maior dos dois valores.
Se forem iguais, a função deve devolver esse valor. Faça três chamadas
com pares de números diferentes.
'''

def maior_numero(a, b):
    if a >= b:
        return a
    else:
        return b


resultado1 = maior_numero(7, 23)
resultado2 = maior_numero(3, 13)
resultado3 = maior_numero(20, 27)

print(f"O maior entre 7 e 23 é: {resultado1}")
print(f"O maior entre 3 e 13 é: {resultado2}")
print(f"O maior entre 20 e 27 é: {resultado3}")