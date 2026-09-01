valor_compra = float(input("Digite o valor do compra: "))
valor_desconto = valor_compra - (valor_compra * 0.10)
if valor_compra > 500:
    print("Desconto disponivel! Fica {:.2f}".format(valor_desconto))
else:
    print("Não vai ter desconto!")