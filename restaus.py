class cadastro:
    def __init__(self):
        self.nome=''
        self.status=''
    def dados():
        self.nome=str((input)("insira o nome:"))
        self.status=int((input)("insira status:"))

opcao=int(input("=========restaurante=========\n1.funcionarios\n2.mesas\n3.pratos\n4.cardapios\n5.desligar"))
while opcao not in [1, 2, 3, 4, 5]:
    print("nao é uma opcao")
    opcao=int(input("Digite outro numero para escolher\n1.funcionarios\n2.mesas\n3.pratos\n4.cardapios\n5.desligar"))
if opcao==1:
    fun=(input("1.Para novo funcionario\n2.Status\n3.Alterar status\n4.sair"))
        if fun==1:
            
        elif fun==2:
        
        elif fun==3:
        
        elif fun==4:
        
elif opcao==2:
    mes=(input("1.Status\n2.A-lterar status\n3.sair"))
        if mes==1:
        
        elif mes==2:
        
        elif mes==3:
        
elif opcao==3:
    pra=(input("1.Para novo prato\n2.sair"))
    if pra==1:

    elif pra==2:

elif opcao==4:
    car=(input("1.mostrar cardapio\n2.pedir prato\n3.sair"))
        if car==1:

        elif car==2:  

        elif car==3:    
elif opcao==5:
