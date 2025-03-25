senha=1234
x=0
extrato=0

senha1=int(input("dgt a senha "))

if senha == senha1:
        while x!=1:
                opcao=int(input("dgt a opção que deseja\n 1-Extrato\n 2-Deposito\n 3-Saque\n 4-Adm\n 5-Sair"))
   
                if opcao==1:
                        print("O saldo da sua conta e ",extrato)

                elif opcao==2:
                        deposito=float(input("dgt o valor do deposito\n"))
                        extrato=deposito+extrato

                elif opcao==3:
                        saque=float(input("dgt o valor do Saque\n"))
                        extrato=extrato-saque

                elif opcao==4:
                        cadastro=int(input("1-Cadastro\n Editar Cadastro"))

                        if cadastro==1:
                                nome=input("dgt seu nome")
                                cpf=input("dgt seu cpf")
                                fone=input("dgt seu telefone")
                                sexo=input("dgt seu sexo")

                        elif cadastro==2:
                                nome=input("dgt seu nome")
                                cpf=input("dgt seu cpf")
                                fone=input("dgt seu telefone")
                                sexo=input("dgt seu sexo")
                
                elif opcao==5:
                        print("Saindo...")
                        x=1

                 
                else:
                        print("opção dgt invalida")
if senha != senha1:
        print("Senha inválida")
