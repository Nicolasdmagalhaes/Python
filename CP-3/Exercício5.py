contratos = []
def calcular_financiamento(vlr_emprestimo, tx_juros, meses):
    valor = vlr_emprestimo
    evolucao = []
    for _ in range(meses):
        valor *= 1 + (tx_juros/100)
        evolucao.append(valor)

    valor_parcela = valor / meses

    return valor, valor_parcela, evolucao

def realizar_simulacao():
    valor = float(input("Digite o valor do empréstimo R$: "))
    tx = float(input("Digite o valor da taxa de juros (%): "))
    meses = int(input("Digite a quantidade de meses: "))

    total, parcela, evolucao = calcular_financiamento(valor, tx, meses)

    for i in range(len(evolucao)):
        print(f"Mês {i+1}: R$ {evolucao[i]:.2f}")

    print(f"Valor total financiado: R$  {total:.2f}")
    print(f"Valor de cada parcla: R$ {parcela:.2f}")

    contratos.append(total)

def consultar_contratos():
    print("Quantidade de contratos simulados: ", len(contratos))
    print("Valor total financiado: ", sum(contratos))

def main():
    while True:
        print("---MENU---")
        print("1 - Realizar nova simulação")
        print("2 - Consultar contratos realizados")
        print("3 - Encerrar")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            realizar_simulacao()
        elif opcao == 2:
            consultar_contratos()
        elif opcao == 3:
            break
        else:
            print("Opção invalida!")


if __name__ == "__main__":
    main()