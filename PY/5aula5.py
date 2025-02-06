x=int(input("DGT UM VALOR "))
y=int(input("DGT UM VALOR "))
z=int(input("DGT UM VALOR "))

if x>y:
    if y>z:
        print(x,y,z)
    elif z>y:
        print(x,z,y)

if z>x:
    if y>x:
        print(z,y,x)

    elif x>y:
        print(z,x,y)

if y>x:
    if x>z:
        print(y,x,z)

    elif z>x:
        print(y,z,x)







