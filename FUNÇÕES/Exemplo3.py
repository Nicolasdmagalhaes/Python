# 1. Crianado uma função com variavel globa, sendo redeclarada na global

def alterar(n1):
    n1 = n1 +1
    print("Dentro da função: ", n1)

# 2. Fora da função, o código não muda a função!
n1 = 10

alterar(n1)

print("Fora da função: ", n1 )