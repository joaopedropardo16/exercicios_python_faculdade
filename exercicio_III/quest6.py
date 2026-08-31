v_compra = float(input("Informe o valor da compra: R$"))

if v_compra >= 500:
    v_compra -= v_compra*0.1
    print(f"Valor com desconto: R${v_compra}")
else:
    print("Sem desconto disponivel")
    print(f"Valor: R${v_compra}")    