from datetime import datetime
dados = dict()

while True:

    dados['nome'] = str(input("Nome: "))
    nasc = int(input("Ano de Nascimento: "))
    dados['idade'] = datetime.now().year - nasc
    dados['sexo'] = str(input("Sexo: "))
    dados['telefone'] = int(input("Telefone: "))
    dados['email'] = input("Email/Gmail: ")
    dados['proprietário'] = str(input("Proprietário: "))
    dados['identificação'] = str(input("Indentificação: "))
    dados['condomínio'] = input("Condomínio: ")
    dados['endereço'] = input("Endereço: ")
    dados['despesas'] = int(input("Despesas: "))
    dados['editar despesa'] = str(input("Deseja editar suas despesas? "))
    if dados['editar despesa'] in "Ss":
        dados['despesas'] = int(input("Despesas:"))
    dados['finalizar'] = str(input("Deseja continuar? [S/N]: "))
        
    if dados['finalizar'] not in "Ss":
        break
    
for k, v in dados.items():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"  -> {k} tem o valor {v}.")