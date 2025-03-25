class Super:
    def __init__(self):
        self.nome=input("DGT seu nome: ")
        self.telefone=input("DGT seu telefone: ")
        self.endereço=input("DGT seu endereço: ")
        self.email=input("DGT seu email: ")
    
class Pessoa(Super):
    def PF(self):
        self.cpf=int(input("DGT seu cpf: "))
        self.Data_Nas=input("DGT seu Data de nascimento: ")
        self.E_civil=input("DGT seu estado civi: ")
        print(f"{self.nome}\n{self.cpf}\n{self.telefone}\n{self.email}\n{self.Data_Nas}\n{self.E_civil}")

class Empresa(Super):
    def PJ(self):
        self.cnpj=int(input("DGT o numemo do cnpj: "))
        self.Junta_Comercial=input("DGT o numemo da Junta_Comercial: ")
        self.Contrato_social=input("DGT o numemo do Contrato_social: ")
        self.Inscrição_Estadual=input("DGT o numemo da Inscrição_Estadual: ")
        self.Inscrição_Municipal=input("DGT o numemo daInscrição_Municipal: ")

        print(f"{self.nome}\n{self.Junta_Comercial}\n{self.Contrato_social}\n{self.cnpj}\n{self.Inscrição_Estadual}\n{self.Inscrição_Municipal}")


    

        













