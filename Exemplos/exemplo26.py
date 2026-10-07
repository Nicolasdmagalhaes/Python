contador = 0
while contador < 16:
    contador += 1
    if contador % 2 != 0:  # ímpar
        continue
    print(contador)

print('Fora do laço')