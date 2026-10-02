salario = float(input("Digite o salário: R$ "))
# Cálculo do INSS
if salario <= 1621:
    inss = salario * 0.075 - 00.0
elif salario <= 2902.84:
    inss = salario * 0.09 - 24.32
elif salario <= 4354.27:
    inss = salario * 0.12 - 111.40
elif salario <= 8475.55:
    inss = salario * 0.14 - 198.49
else:
    inss = 8475.55 * 0.14 - 198.49
# Cálculo do IR
# Primeiro descontamos o INSS para encontrar a base do IR
base_ir = salario - inss
if base_ir <= 2259.20:
    ir = 0
elif base_ir <= 2826.65:
    ir = base_ir * 0.075 - 182.16
elif base_ir <= 3751.05:
    ir = base_ir * 0.15 - 394.16
elif base_ir <= 4664.68:
    ir = base_ir * 0.225 - 675.49
else:
    ir = base_ir * 0.275 - 908.73
# Salário líquido
salario_liquido = salario - inss - ir

print(f"INSS: R$ {inss:.2f}")
print(f"IR: R$ {ir:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
