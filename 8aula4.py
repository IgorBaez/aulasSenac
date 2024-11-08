while True:
    nome=input("DGT seu nome ")
    if len(nome)<4:
        print("nome invalido ")
        nome=input("DGT seu nome ")
        continue
    idade=int(input("DGT sea idade "))
    if idade <0 or idade>150:
        print("idade invalida ")
        continue
    sala=float(input("DGT seu salario "))
    if sala<=0:
        print("salario invalido ")
        continue
    sexo=int(input("DGT seu sexo 1-masculino ou 2-feminino "))
    if sexo !=1 and sexo!=2:
        print("sexo invalido ")
        continue
    civil=int(input("DGT seu estatos civil 1-solteiro 2-casado 3-viuvo 4-divorciado "))
    if civil<0 and civil>4:
        print("estado civil invalido ")
        continue





