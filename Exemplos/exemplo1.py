nome = input("Digite seu nome: ")
print(nome,type(nome))

idade = input("Digite a sua idade:")
print(idade,type(idade))

# Toda informação que é enviada ou recuperada ddo terminal é str (string, mesmo que texto)
#Função ded coverção
#Numeros inteiros int()
#Numeros decimais float()

idade = int(input("Digite sua idade (0 até 100) "))
print(idade,type(idade))


altura = float(input("Digite sua altura: "))
print(altura,type(altura))

situacao = bool(input("Digite 0 para sair ou 1 para manter Ativo: "))
print(situacao,type(situacao))
# no bool é esperado 1 - true 0 - falso

verdadeiro = True
falso = False
print(type(verdadeiro),type(verdadeiro))

# Na programação temos as seguintes tipagem: Texto, Numeros e Booleanos