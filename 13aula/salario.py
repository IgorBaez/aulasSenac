
def salarioAumento(valor,aumento):
    nv=valor+(valor*aumento/100)
    return nv

def salarioDesconto(valor,c):
    nv=valor-(valor*c/100)
    return nv
print(salarioDesconto(1000,10))









