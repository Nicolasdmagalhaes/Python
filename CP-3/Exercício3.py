def calcular_media(lista):
    # media = soma/quantidade
    # sum: somar
    # len: o tamanho ou quantidade
    media = sum(lista) / len(lista)
    return media

def main():
    notas = []

    while True:
        nota = float(input("DIgite uma nota (-1 para encerrar): "))

        if nota == -1:
            break
        if nota>=0 and nota<=10:
            notas.append(nota)
        else:
            print("Nota inválida")

    if len(notas) == 0:
        print("Nenhuma nota foi cadastrada")
    else:
        print("Quantidade: ", len(notas))
        print("Média: ", calcular_media(notas))
        print("Maior nota: ", max(notas))
        print("Menor nota: ", min(notas))


if __name__ == "__main__":
    main()