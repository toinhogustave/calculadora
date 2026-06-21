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
    while b<=0:
        print("nao")
        b=float(input('digite o outro valor:'))
    print(f'a divisão é:{a/b}')
elif opcao==5:
    a=float(input('digite o valor do produto:'))
    while a<=0:
        print("nao")
        a=float(input('digite o valor do produto novamente:'))
    b=float(input('insira o pagamento:'))
    while b<=0:
        print("nao")
        b=float(input('digite o valor do pagamento novamente:'))
    if b<a:
        print("nao é possvel pagar,dinheiro não suficiente")
    else:
        j=b-a
        r= int(j)
        c = round((j - r) * 100)
        print(f"o troco é:\ncedulas:{r}\nmoedas:{c}")
elif opcao==6:
    a=int(input('digite a velocidade do objeto:'))
    while a<=0:
        print("nao")
        a=float(input('digite o velocidade do objeto:'))
    b=int(input('digite a inclinaçao em graus do objeto:'))
    while b<=0:
        print("nao")
        b=float(input('digite a inclinaçao em graus do objeto:'))
    c=int(input('digite o tempo em que o objeto ficou no ar:'))
    while c<=0:
        print("nao")
        c=float(input('digite a inclinaçao em graus do objeto:'))    
    r=(b*3.14159)/90
    x=a*r*c
    f=(r-r*r*r/6 + r*r*r*r*r/120)
    print(f'a posiçao de queda com 10 m/s para a gravidade é:{(a*a*f)/10:.2f} metros\n O lançamento horizontal é:{x:.2f} metros')