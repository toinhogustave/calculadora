opcao=int(input("=========calculadora=========\n1.soma\n2.subtracao\n3.multiplicaçao\n4.divisão\n5.Fluxo de Caixa\n6.Cálculo de posição de queda de um projétil\nEscolha uma das opções:"))
while opcao not in [1, 2, 3, 4, 5, 6]:
    print("nao é uma opcao")
    opcao=int(input("Digite outro numero para escolher\n1.soma\n2.subtracao\n3.multiplicaçao\n4.divisão\n5.Fluxo de Caixa\n6.Cálculo de posição de queda de um projétil\nEscolha uma das opções:"))
    
if opcao==1:
    a=int(input('digite um valor:'))
    b=int(input('outro valor:'))
    print(f'a soma é:{a+b}')
elif opcao==2:
    a=int(input('digite um valor:'))
    b=int(input('outro valor:'))
    print(f'a subtração é:{a-b}')
elif opcao==3:
    a=int(input('digite um valor:'))
    b=int(input('outro valor:'))
    print(f'a multiplicação é:{a*b}')
elif opcao==4:
    a=int(input('digite um valor:'))
    b=int(input('outro valor:'))
    print(f'a divisão é:{a/b}')
elif opcao==5:
    fluxo(a,b)
elif opcao==6:
    queda(a,b)