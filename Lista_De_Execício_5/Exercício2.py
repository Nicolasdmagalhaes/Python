'''
2. Crie um Algoritmo que que solicite ao utilizador um valor em Reais (R$)
e a sigla de uma moeda estrangeira para conversão. Usa match-case
para definir a taxa de câmbio:
• USD" (Dólar): Multiplicar por 0.20
• "EUR" (Euro): Multiplicar por 0.18
• "GBP" (Libra): Multiplicar por 0.15
• Caso padrão: Exibir "Moeda não suportada".
'''
valor = float(input("Digite o valor em Reais (R$): "))
moeda = input("Digite a sigla da moeda (USD, EUR, GBP): ").lower()

match moeda:
    case "usd":
        resultado = valor * 0.20
        print(f"R$ {valor:.2f} = US$ {resultado:.2f} (Dólar)")
    case "eur":
        resultado = valor * 0.18
        print(f"R$ {valor:.2f} =  EU$ {resultado:.2f} (Euro)")
    case "gbp":
        resultado = valor * 0.15
        print(f"R$ {valor:.2f} = LI$ {resultado:.2f} (Libra)")
    case _:
        print("Moeda não suportada")