p1=int(input("Telefonou para a vitima? \n1-Sim\n0-Não\n"))
p2=int(input("Esteve no local do crime? \n1-Sim\n0-Não\n"))
p3=int(input("Mora perto da vitima? \n1-Sim\n0-Não\n"))
p4=int(input("Devia para a vitima? \n1-Sim\n0-Não\n"))
p5=int(input("ja trabalhou com a vitima? \n1-Sim\n0-Não\n"))
p=p1+p2+p3+p4+p5

if p==2:
    print("Suspeito")

elif p==3 or p==4:
    print("Cumplice")

elif p==5:
    print("Assasino")

else:
    print("Inocente")
















