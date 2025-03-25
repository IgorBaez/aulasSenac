class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
    
class Sub:
    def hello(self):
        print("Olá, sou a subclasse!")

class Subsub:
    def hello(self):
        print("Olá, sou a subsubclasse!")

teste1=Super()
teste1.hello()

teste=Sub()
teste.hello()

teste1=Subsub()
teste1.hello()






