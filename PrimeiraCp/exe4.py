salario = float(input('Digite seu salário: R$'))
if salario < 0:
    al = 0.00
    dedu = 00
elif salario <= 1621.00:
    al = 0.075
    dedu = 0.0
elif salario <=2902.84:
    al = 0.09
    dedu = 24,32
elif salario <=4354.27:
    al = 0.12
    dedu = 111.40
elif salario >=8475.55:
    al = 0.14
    dedu = 198.49
else:
    #teto máximo de contribuição
    salario = 8475.55
    al = 0.14
    dedu = 198.49

inss = (salario *al) - dedu
print(f"INSS: R$ {inss:.2f}")
