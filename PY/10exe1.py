# dados={}
# dados={"gustavo":28,"igor":23,"rafael":17,"jhonatan":17,"jamily":21}
# for i in dados:
#     print(i,"-", dados[i])

try:
   a=int(input("dgt uma palavra "))
except ValueError:
    print("dgt apenas numeros")
except:
   print("erro desconhecido")
finally:
   print("final do algoritmo")






