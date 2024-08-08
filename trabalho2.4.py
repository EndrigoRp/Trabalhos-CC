#============ Imprimir nome completo e o menu ==========================
print("---- Bem-vindo a Loja de Marmitas do Endrigo Rafael Pusch ------")
print("------------------------------Cardápio--------------------------")
print("----------------------------------------------------------------")
print("---| Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---")
print("---|    P     |       R$ 16.00       |       R$ 15.00       |---")
print("---|    M     |       R$ 18.00       |       R$ 17.00       |---")
print("---|    G     |       R$ 22.00       |       R$ 21.00       |---")
print("----------------------------------------------------------------")

# ====== Dicionarios com preços =================
precos = {
    'BA': {'P': 16.00, 'M': 18.00, 'G': 22.00},
    'FF': {'P': 15.00, 'M': 17.00, 'G': 21.00},
}

total = 0

#==== loop principal para pedidos ======
while True:
    # === Sabor e validacao ===
    while True:
        sabor = input("Entre com o sabor desejado (BA/FF): ").strip().upper()
        if sabor in precos:
            break
        else:
            print("Sabor invalido. Tente novamente.\n")
    # === Tamanho e validacao ===
    while True:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").strip().upper()
        if tamanho in precos[sabor]:
            break
        else:
            print("Tamanho invalido. Tente novamente.\n")

    # === if-elif atribuindo valor a variavel preco ===
    if sabor == 'BA':
        if tamanho == 'P':
            preco = precos[sabor][tamanho]
        elif tamanho == 'M':
            preco = precos[sabor][tamanho]
        elif tamanho == 'G':
            preco = precos[sabor][tamanho]
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = precos[sabor][tamanho]
        elif tamanho == 'M':
            preco = precos[sabor][tamanho]
        elif tamanho == 'G':
            preco = precos[sabor][tamanho]

    #=== acumulando valores ===
    total += preco

    print("Você pediu um {} no tamanho {}: R$ {:.2f}\n".format(
        "Bife Acebolado" if sabor == 'BA' else "Filé de Frango",
        tamanho, preco))

    while True:
        mais_alguma_coisa = input("Deseja mais alguma coisa? (S/N): ").strip().upper()
        if mais_alguma_coisa in ["S", "N"]:
            break
        else:
            print("Resposta invalida. Tente novamente.")

    if mais_alguma_coisa == 'N':
        break
    elif mais_alguma_coisa == 'S':
        continue

print("\nO valor total a ser pago: R$ {:.2f}".format(total))