

nome=input("Digite o nome do item: ")
quant=int(input("Digite a quantidade: "))
valor=float(input("Digite o valor: "))
desc=int(input("Digite o desconta: "))

desct=(valor*quant)*(desc/100)
valort=(valor*quant)-desct

print("O item ",nome," custou ",valort)





