idade = int(input('Digite sua idade:'))

#Condicional simples 'IF'
if (idade >= 18):
    print('Acesso permitido')
#Condicional composta 'IF e ELSE'
if (idade >= 18):
    print('Acesso permitido')
else:
    print('Acesso negado')
#Condicional Encadeada '(só tem 1)IF + ELIF(pode ter vários,dentro do if e else) + (só tem 1)ELSE'
Nota = float(input('Digite sua nota:'))
if Nota >= 60:
    print('Aprovado')
elif Nota >= 40:
    print("Exame")
else:
    print('Reprovado')