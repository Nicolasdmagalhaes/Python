contador = 1
while contador <10:
# Começa com 2 por causa do contador+=1
    contador += 1
    #contador +=1 Antes do break não exibe o 5
    if contador == 5:
        print('Pulei o número 5!')
        continue # força o laço realizar a verificação da condição (ou pular um loop)

    print(contador)
  #contador = contator +1

print('Fora do laço')
