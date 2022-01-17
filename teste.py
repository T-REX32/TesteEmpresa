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

    dados['tipo_de_despesa'] = str(input("Qual o tipo de despesa? (água, esgoto, luz, gás e condomínio): "))

    if dados['tipo_de_despesa'] == "água":
        dados['despesas_da_água'] = float(input("Despesas da água: "))

    elif dados['tipo_de_despesa'] == "esgoto":
        dados['despesas_do_esgoto'] = float(input("Despesas do esgoto: "))

    elif dados['tipo_de_despesa'] == "luz":
        dados['despesas_da_luz'] = float(input("Despesas da luz: "))
    
    elif dados['tipo_de_despesa'] == "gás":
        dados['despesas_do_gás'] = float(input("Despesas do gás: "))

    elif dados['tipo_de_despesa'] == "condomínio":
        dados['despesas_do_condomínio'] = float(input("Despesas do condomínio: "))

    dados['editar_despesa'] = str(input("Deseja editar suas despesas? "))

    if dados['editar_despesa'] in "Ss":
        dados['tipo_de_despesa'] = str(input("Qual o tipo de despesa? (água, esgoto, luz, gás e condomínio): "))

    if dados['tipo_de_despesa'] == "água":
        dados['despesas_da_água'] = float(input("Despesas da água: "))

    elif dados['tipo_de_despesa'] == "esgoto":
        dados['despesas_do_esgoto'] = float(input("Despesas do esgoto: "))

    elif dados['tipo_de_despesa'] == "luz":
        dados['despesas_da_luz'] = float(input("Despesas da luz: "))
    
    elif dados['tipo_de_despesa'] == "gás":
        dados['despesas_do_gás'] = float(input("Despesas do gás: "))

    elif dados['tipo_de_despesa'] == "condomínio":
        dados['despesas_do_condomínio'] = float(input("Despesas do condomínio: "))
    
    dados['vencimento_fatura'] = int(input("Escolha o dia do vencimento de sua fatura (quantos dias para o vencimento): "))

    dados['finalizar'] = str(input("Deseja continuar? [S/N]: "))
    if dados['finalizar'] not in "Ss":
        break
    
for k, v in dados.items():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"  -> {k} tem o valor {v}.")