total=0
while True:

    while True:
        y=float(input("valor do item "))
        total=total+y
        if y==0.0:
            break
    print(total)
    while True:
        x=float(input("valor do pagamento "))
        if total>x:
            print("Valor insuficiente ")
        elif total<=x:
            z=x-total
            print("Seu troco foi de ",z) 
            total=0
            break
    x=int(input("DGT 0-Sair ou qualquer tecla para continuar "))
    if x==0:
        print("Saindo...")
        break








