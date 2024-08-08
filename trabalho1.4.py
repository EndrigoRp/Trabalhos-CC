#========= Input do Usuario ==========
print("Bem-vindo a Loja do Endrigo Rafael Pusch")
valor_doPedido = float(input("Entre com o valor do pedido: "))
qtd_parcelas = int(input("Entre com a quantidade de parcelas: "))

#========= juros com base na qtd de parcelas =============
if qtd_parcelas < 4:
    juros = 0.0
elif qtd_parcelas >= 4 and qtd_parcelas < 6:
    juros = 0.04
elif qtd_parcelas >= 6 and qtd_parcelas < 9:
    juros = 0.08
elif qtd_parcelas >= 9 and qtd_parcelas < 13:
    juros = 0.16
else:
    juros = 0.32

#========= Calculo da parcela com base no juros ============
valor_daParcela = (valor_doPedido * (1 + juros)) / qtd_parcelas

#======== Calculo do valor total parcelado ==========
valor_totalParcelado = valor_daParcela * qtd_parcelas

#======== Condiçao de valores total com base nos juros e parcelas ====
if qtd_parcelas >= 4:
    print(f"Valor da Parcela: R$ {valor_daParcela:.2f}")
    print(f"Valor Total Parcelado: R$ {valor_totalParcelado:.2f}")
else:
    print(f"O valor das parcelas é de: R$ {valor_daParcela:.2f}")
    print(f"O valor Total Parcelado é de: R$ {valor_totalParcelado:.2f}")