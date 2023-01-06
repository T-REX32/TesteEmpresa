from datetime import datetime
dados = dict()
soma = 0
while True:

    dados['nome'] = str(input("Nome: "))

    nasc = int(input("Ano de Nascimento: "))

    dados['idade'] = datetime.now().year - nasc

    dados['sexo'] = str(input("Sexo: "))
    while dados['sexo'] not in "MmFf":
        dados['sexo'] = str(input("Sexo (M-masculino ou F-feminino): "))

    dados['telefone'] = int(input("Telefone: "))
    
    dados['email'] = input("Email/Gmail: ")

    dados['proprietário'] = str(input("Proprietário: "))

    dados['identificação'] = str(input("Indentificação: "))

    dados['condomínio'] = input("Condomínio: ")

    dados['endereço'] = input("Endereço: ")

    dados['despesas_da_água'] = float(input("Despesas Água: "))

    dados['despesas_do_esgoto'] = float(input("Despesas do esgoto: "))

    dados['despesas_da_luz'] = float(input("Despesas da luz: "))
        
    dados['despesas_do_gás'] = float(input("Despesas do gás: "))
    
    dados['despesas_do_condomínio'] = float(input("Despesas do condomínio: "))

    soma = dados['despesas_da_água'] + dados['despesas_do_esgoto'] + dados['despesas_da_luz'] + dados['despesas_do_gás'] + dados['despesas_do_condomínio']
    print(f"R${soma} para pagar.")

    dados['editar_despesa'] = str(input("Deseja editar suas despesas? "))

    if dados['editar_despesa'] in "Ss":

        dados['despesas_da_água'] = float(input("Despesas Água: "))

        dados['despesas_do_esgoto'] = float(input("Despesas do esgoto: "))

        dados['despesas_da_luz'] = float(input("Despesas da luz: "))
            
        dados['despesas_do_gás'] = float(input("Despesas do gás: "))
        
        dados['despesas_do_condomínio'] = float(input("Despesas do condomínio: "))

        soma = dados['despesas_da_água'] + dados['despesas_do_esgoto'] + dados['despesas_da_luz'] + dados['despesas_do_gás'] + dados['despesas_do_condomínio']
        print(f"R${soma} para pagar.")

    dados['vencimento_fatura'] = int(input("Escolha o dia do vencimento de sua fatura (quantos dias para o vencimento): "))
    break
    
for k, v in dados.items():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"  -> {k} tem o valor {v}.")
print("Cadastro finalizado.")