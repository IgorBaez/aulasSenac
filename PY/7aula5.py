litro=int(input("Quantos litros ?"))
conb=input("g-gasolina \na-alcool\n")

if conb=="a":
    if litro <=20:
        valor=litro*1.90
        desc=valor*0.03
        total=valor-desc
        print(total)

    if litro>20:
        valor=litro*1.90
        desc=valor*0.05
        total=valor-desc
        print(total)


if conb=="g":
    if litro <=20:
        valor=litro*2.50
        desc=valor*0.04
        total=valor-desc
        print(total)

    if litro>20:
        valor=litro*2.50
        desc=valor*0.06
        total=valor-desc
        print(total)












