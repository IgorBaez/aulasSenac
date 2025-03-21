while True:
    while True:
        try:
            a=float(input("dgt o primeiro valor "))
            b=float(input("dgt o segundo valor "))
            if a==0 or b==0:
                print("valores digitados invalidos")
                continue
            break
        except:
            print("dgt apenas numeros")

    try:
        c=int(input("1-multiplicação\n2-divisão\n3-subitração\n4-soma\n0-sair\n"))
        if c==1:
            c=a*b
            print("resultado ",c)
        elif c==2:
            c=a/b
            print("resultado ",c)
        elif c==3:
            c=a-b
            print("resultado ",c)
        elif c==4:
            c=a+b
            print("resultado ",c)
        elif c==0:
            break
    except:
         print("dgt apenas numeros")













