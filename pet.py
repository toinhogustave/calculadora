lista=[]
cadastro={'nome': '', 'idade': 0, 'sexo': ''}
soma=0
for c in range (0,2):
    cadastro['nome']=str((input)("insira o nome:"))
    cadastro['idade']=int((input)("insira a idade:"))
    soma+=cadastro['idade']
    cadastro['sexo']=str((input)("insira o sexo (apenas M ou F):"))
    lista.append(cadastro.copy())
print(f"o numero da media de idades é:{soma/len(lista)}")
print(f"numero de pessoas cadastrada foi de {len(lista)}")
for p in lista :
    if p['sexo'] in 'Ff':
        print(f'nome da mulher é: {p['nome']}')
for p in lista:
    if p['idade'] >=soma/len(lista):
        print(f"{p['nome']} tem idade maior que a media")