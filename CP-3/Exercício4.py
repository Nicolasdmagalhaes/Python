placas = []
tipos_veiculos = []

faturamento = 0
horas =0
subtotal = 0
desconto = 0
total_pagar = 0
placa = ""
tipo = ""

def registrar_entrada():
        global placa, tipo

        placa = input("Digite a placa: ")

        print("1 - Carro")
        print("2 - Moto")
        print("3 - Caminhonete")

        tipo = int(input("Digite o tipo do veículo: "))

        placas.append(placa)
        tipos_veiculos.append(tipo)

        print("Entrada registrada com sucesso!")

def registrar_saida():
    global horas, subtotal, desconto, total_pagar

    placa_saida = input("Digite a placa do veículo: ")

    # Procurando o veículo dentro da lista
    if placa_saida not in placas:
        print("Veiculo não encontrado!")

    # Procurando o veiculo dentro da lista e obtendo o seu index
    i = placas.index(placa_saida)
    tipo_veiculo = tipos_veiculos[i]

    horas  = int(input("Digite a quantidade de horas: "))
    # calculo de horas
    if tipo_veiculo == 1:
        subtotal = horas * 8
    elif tipo_veiculo == 2:
        subtotal = horas * 5
    else:
        subtotal = horas * 12

    #calculo do desconto
    if horas <= 2:
        desconto =0
    elif horas <=5:
        desconto = subtotal * 0.05
        #desconto de 5%
    else:
        desconto = subtotal * 0.10
        #desconto de 10%

    total_pagar = subtotal - desconto

    #Removendo o veiculo da lista
    placas.pop(i)
    tipos_veiculos.pop(i)

    print("Subtotal da estadia: ", subtotal)
    print("Desconto aplicado: ", desconto)
    print("Total a pagar: ", total_pagar)
    return total_pagar

def main():
    global faturamento
    while True:
        print("------ MENU -------")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Ver faturamento")
        print("4 - Encerrar")
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            registrar_entrada()
        elif opcao == 2:
           faturamento += registrar_saida()
        elif opcao == 3:
            print("Faturamento acumulado: ", faturamento)
        elif opcao == 4:
            print("Faturamento acumulado: ", faturamento)
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

