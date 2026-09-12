# Trabalhando com texto atraves do print

#Texto em Python pode ser aspas simples ' ' ou compostas" "
nome = "Nicolas David"
curso = 'ADS'
idade = 20
print(nome, curso)

#Juntar texto ou concatenar texto
# é utilizado o operador +
print("Nome: "+nome+" Curso: "+curso)


# f-string (format-string), dentro ded um texto { }
print(f"Nome: {nome} Curso: {curso} Idade: {idade}")

#Quebras de linhas \n
print(f"Nome: {nome}\nCurso: {curso}\nIdade: {idade}")

#Utilizando aspas dentro ddo texto, inverter o uso das aspas
#Utiliazndo aspas simples para edfinição ed texto e aspas dulpas ddentro ddo texto

print('Nome: '+nome+'  "Curso: " '+curso)

#tubulação poded utilizar \t
print('Nome:\tNicolas\tDavid')