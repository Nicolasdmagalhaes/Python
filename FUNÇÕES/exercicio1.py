'''def contar_caracteres(palavra):
    return len(palavra)


texto = input("Digite uma palavra: ")
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.") '''


def saudacao(hora):
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


hora_atual = int(input("Digite a hora atual (0-23): "))
print(saudacao(hora_atual))