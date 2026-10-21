'''
5. Crie a função calcular_preco_final(preco, percentual), que devolva o
preço após o desconto. Solicite os dois valores ao usuário e exiba o
preço original, o valor descontado e o preço final.
'''

def calcular_preco_final(preco, percentual):
     desconto = preco * percentual / 100
     preco_final = preco - desconto
     return preco_final

preco = float(input("Digite o preço original: "))
percentual = float(input("Digite o percentual de desconto: "))

preco_final = calcular_preco_final(preco, percentual)
valor_descontado = preco - preco_final

print(f"Preço original: R$ {preco:.2f}")
print(f"Valor descontado: R$ {valor_descontado:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")