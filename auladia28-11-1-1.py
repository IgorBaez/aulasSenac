from auladia28 import*

x=int(input("DGT 1 para pesoa fisica\nDGT 2 para pessoa juridican\n"))
if x==1:
    pessoa1=Pessoa()
    pessoa1.PF()
    
else:
    pessoa1=Empresa()
    pessoa1.PJ()


