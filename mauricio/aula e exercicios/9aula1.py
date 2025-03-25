a=int(input("DGT a populaçao da cidade A "))
b=int(input("DGT a populaçao da cidade B "))
c=float(input("DGT a taxa de crescimento(em porcentagem) da cidade A "))
d=float(input("DGT a taxa de crescimento(em porcentagem) da cidade B "))
c=(c/100)
d=(d/100)
count=0

while True:
    a+=a*c
    b+=b*d
    count+=1
    if a>=b:
        break
print(count)
print(a)











