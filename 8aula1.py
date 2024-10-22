#b=int(input("dgt un numero de 0 a 10 : "))
#while b<11:
#    print("baz")
#    b=b+1
#print("Fim")

#while True:
#    valor=int(input("Dgt 1 para conti 0 para fim "))
#    if valor>=1:
#        continue
#        print("valor correto")
#    else:
#        print("Valor para sair ")
#       break

i=0
while i==0:
    opcao=int(input("1-multiplicação\n2-divisão\n3-soma\n4-subitração\n5-sair\n"))
    if opcao==1:
        a1=float(input("dgt o primeiro valor "))
        a2=float(input("dgt o primeiro valor "))
        a3=a1*a2
        print("o resultado e ",a3)
    elif opcao==2:
        a1=float(input("dgt o primeiro valor "))
        a2=float(input("dgt o primeiro valor "))
        a3=a1/a2
        print("o resultado e ",a3)
    elif opcao==3:
        a1=float(input("dgt o primeiro valor"))
        a2=float(input("dgt o primeiro valor"))
        a3=a1+a2
        print("o resultado e ",a3)
    elif opcao==4:
        a1=float(input("dgt o primeiro valor "))
        a2=float(input("dgt o primeiro valor "))
        a3=a1-a2
        print("o resultado e ",a3)
    elif opcao==5:
        print("Saindo....")
        i=1
    else:
        print("valor invalido")











