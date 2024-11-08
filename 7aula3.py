nota=float(input("dgt a nota1  "))
nota1=float(input("dgt a nota2  "))
nota2=float(input("dgt a nota3  "))
nota3=float(input("dgt a nota4  "))
media=(nota+nota1+nota2+nota3)/4

if media<=10 and media>=9.1:
    print("Sua media foi de",media," aproveitamento: A aprovado")

elif media<9.1 and media>=7.6:
    print("Sua media foi de",media," aproveitamento: B aprovado")

elif media<=7.5 and media>=6:
    print("Sua media foi de",media," aproveitamento:  C aprovado")

elif media<=5.9 and media>=4.1:
    print("Sua media foi de",media," aproveitamento: D reprovado")

elif media<=4 and media>=0:
    print("Sua media foi de",media," aproveitamento: E reprovado")











