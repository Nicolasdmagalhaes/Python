salario = float(input('Digite seu salário: R$'))
if salario < 0:
    al = 0.0
    dedu = 0.00
elif salario <= 2428.80:
    al = 0.0
    dedu = 0.00
elif salario <= 2826.65:
    al = 0.075
    dedu = 182.16
elif salario <= 3751.05:
    al = 0.015
    dedu = 394.16
elif salario <= 4664.68:
    al = 0.225
    dedu = 675.49
elif salario >=4664.68:
    al = 0.275
    dedu = 908.73
else:
    salario >=4664.68
    al = 0.275
    dedu = 908.73

IR = (salario * al) - dedu
print(f"IR: R${IR:.2f}")


