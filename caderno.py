pessoa= {'nome':'','idade':0, 'ano': 0, 'salario':0}
pessoa['nome']=str((input)("insira o nome:"))
pessoa['idade']=int((input)("insira a idade:"))
ctps=int (input("tem trabaio? (0 para nem)"))
if ctps== 0:
        print(f'{pessoa["nome"]} e a idade é: {pessoa["idade"]}')
else:
    pessoa['ano']=int((input)("insira ano de contrataçao:"))
    pessoa['salario']=int((input)("salário:"))
    print(f'{pessoa}\nvai se aposentar em:{pessoa["ano"]+51}')