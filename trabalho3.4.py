def escolha_modelo():
    while True:
        print("\nEntre com modelo desejado:")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input("Digite modelo (MCS/MLS/MCE/MLE): ").strip().upper()
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            print("Opção inválida. Por favor, escolha entre MCS, MLS, MCE, MLE")


def num_camisetas():
    while True:
        try:
            num = int(input("Digite o número de camisetas: ").strip())
            if num > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                print("Por favor, entre com o número de camisetas novamente\n.")
            elif num < 20:
                return num, 0
            elif 20 <= num < 200:
                return num, 0.5
            elif 200 <= num < 2000:
                return num, 0.07
            elif 2000 <= num <= 20000:
                return num, 0.12
        except ValueError:
            print("Por favor, insira um numero valido.")


def frete():
    while True:
        print("Escolha o serviço de frete:")
        print("0 - Retirar na fábrica (R$ 0)")
        print("1 - Transportadora (R$ 100)")
        print("2 - Sedex (R$ 200)")
        opcao_frete = input().strip()
        if opcao_frete == '0':
            return 0
        elif opcao_frete == '1':
            return 100
        elif opcao_frete == '2':
            return 200
        else:
            print("Opção inválida. Por favor, escolha entre 0, 1 e 2.")



print("Bem vindos a Fabrica de Camisetas do Endrigo Rafael Pusch")

    #===Variavel recebe funçao Escolha do modelo===
valor_unitario = escolha_modelo()

    #===Variavel recebe funçao Numero de camisetas===
numero_camisetas, desconto = num_camisetas()

    #===Variavel recebe funçao Serviço de frete===
valor_frete = frete()

    #===Calculo do total===
valor_total = (valor_unitario * numero_camisetas) * (1 - desconto) + valor_frete

print(f"\nModelo escolhido: {valor_unitario}")
print(f"Número de camisetas: {numero_camisetas}")
print(f"Desconto aplicado: {desconto*100}%")
print(f"Valor do frete: {valor_frete}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")

