pessoa={'nome': '', 'nota': 0 }
pessoa['nome']=str(input("insira o nome do aluno"))
pessoa['nota']=int(input("insira a nota do aluno"))
if pessoa['nota'] >=7:
    print(f"passou {pessoa['nome']}")
else:
    print(f"nem passou {pessoa['nome']}")