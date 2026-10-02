total_economizado = 0
mes = 1

while mes <= 3:
    valor = float(input(f"Digite o valor a ser economizado no mes {mes} R$: "))
    total_economizado = valor + total_economizado #Acumulador
    mes +=1 #Contator
print('Parabéns! Voce economizou', total_economizado)
#Contador normalmente é utilizado na condição do loop
#Contador sempre incrementa valores por padrão +1, ou +2

#Acumulador pode ser utilizado na condição do loop
#Não soma valores padronizados