'''
2. Implemente duas versões para calcular a média de duas notas:
a. exibir_media(nota1, nota2), que mostra o resultado dentro da
própria função, e
b.  calcular_media(nota1, nota2), que devolve o resultado com
return.
c. Chame as duas versões. Use o valor devolvido pela segunda
para informar “Aprovado” quando a média for maior ou igual a 6 e
“Reprovado” nos demais casos.
'''

# Função 1
def exibir_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"Média (exibida pela função): {media}")


# Função 2
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


exibir_media(7, 5)

media_final = calcular_media(7, 5)
print(f"Média (devolvida pela função): {media_final}")

if media_final >= 6:
    print("Aprovado")
else:
    print("Reprovado")


