def a(x):
    if x>0:
        return "P"
    elif x<0:
        return "N"
    else:
        return "valor igual a 0"
while True:
    num=int(input("um numero "))
    if a(num)=="N":
        print("negativo")
    elif a(num)=="P":
        print("positivo")
    else:
        print(a(num))







