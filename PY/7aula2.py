salario=float(input("dgt o seu salario "))

if salario>= 1500:
    aumento=salario*0.05
    salarioTotal=salario+aumento
    print("Seu salario antigo era de ",salario," o atual e de ",salarioTotal," o aumento foi de 5% ",aumento)

elif salario >700 and salario <1500 :
    aumento=salario*0.10
    salarioTotal=salario+aumento
    print("Seu salario antigo era de ",salario," o atual e de ",salarioTotal," o aumento foi de 10% ",aumento)

elif salario >280 and salario <=700:
    aumento=salario*0.15
    salarioTotal=salario+aumento
    print("Seu salario antigo era de ",salario," o atual e de ",salarioTotal," o aumento foi de 15% ",aumento)

elif salario <= 280:
    aumento=salario*0.20
    salarioTotal=salario+aumento
    print("Seu salario antigo era de ",salario," o atual e de ",salarioTotal," o aumento foi de 20% ",aumento)












