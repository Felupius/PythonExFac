valorCompra = int(input("Qual o valor da compra?"))
valorPago = int(input("Qual o valor pago?"))

troco = valorPago - valorCompra

if valorCompra > valorPago:
    print(f"Pagamento insuficiente, digite um valor acima de R$", valorCompra)
else:
    print(f"Valor do troco foi R$",troco)