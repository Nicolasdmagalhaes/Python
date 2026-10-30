def valida_senha(senha):
    return len(senha)>=8

def main():
    while True:
        senha = input('Digite sua senha: ')

        if valida_senha(senha):
            print('Senha valida!')
            break
        else:
            print('Senha invalida!')

main()