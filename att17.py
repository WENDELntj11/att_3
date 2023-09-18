def calculadora_de_impostos():
    valor_compra = float(input("Insira o valor da compra: "))
    valor_imposto = float(input("Insira o valor do imposto a ser adicionado: "))
    valor_total = valor_compra + valor_imposto
    print("Valor total da compra com imposto:", round(valor_total, 2))

calculadora_de_impostos()