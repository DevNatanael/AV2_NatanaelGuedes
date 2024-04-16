# dicionários para armazenar detalhes da transação
transacoes = {"id": [], "tipo": [], "status": []}
detalhes_conta = {"id": [], "detalhes": []}
detalhes_banco = {"id": [], "detalhes": []}

# Dicionários como expressões lambda
conta_corrente = lambda: {1: 1000, 2: 500, 3: 1200}
senha = lambda: {1: "senha1", 2: "senha2", 3: "senha3"}

# Atualizar valor da conta corrente para um dado usuário
atualizar_conta_corrente = lambda id, novo_valor: conta_corrente().update({id: novo_valor}) if id in conta_corrente() else None

# funções lambda
criar_transacao = lambda id, tipo: [transacoes[chave].append(valor) for chave, valor in {"id": id, "tipo": tipo, "status": "criada"}.items()] and (detalhes_conta["id"].append(id) and detalhes_conta["detalhes"].append(None) if tipo == "credito" else None) and print("Criando transação")

receber_dinheiro = lambda id: [transacoes["status"].__setitem__(transacoes["id"].index(id), "dinheiro recebido") if transacoes["tipo"][transacoes["id"].index(id)] == "dinheiro" else "erro"] and print("Recebendo dinheiro")

solicitar_detalhes_conta = lambda id, detalhes: [detalhes_conta["detalhes"].append(detalhes) if transacoes["tipo"][transacoes["id"].index(id)] == "credito" else "erro"] and print("Solicitando detalhes de crédito da conta")

solicitar_pagamento_banco = lambda id: (transacoes["status"].__setitem__(transacoes["id"].index(id), "pagamento solicitado"), print("Solicitando pagamento do banco")) if transacoes["tipo"][transacoes["id"].index(id)] == "credito" else "erro"

confirmar_pagamento_banco = lambda id, aprovado: (transacoes["status"].__setitem__(transacoes["id"].index(id), "pagamento aprovado"), print("Confirme a aprovação do pagamento do banco")) if aprovado else (transacoes["status"].__setitem__(transacoes["id"].index(id), "pagamento não aprovado"), print("Pagamento não aprovado pelo banco"))

fornecer_detalhes_deposito_banco = lambda id, detalhes: (detalhes_banco["id"].append(id), detalhes_banco["detalhes"].append(detalhes), print("Forneça detalhes de depósito bancário")) if transacoes["status"][transacoes["id"].index(id)] == "pagamento aprovado" else "erro"

transferir_fundos = lambda id: (transacoes["status"].__setitem__(transacoes["id"].index(id), "fundos transferidos"), print("Fundos transferidos")) if transacoes["status"][transacoes["id"].index(id)] == "pagamento aprovado" else "erro"

imprimir_recibo_pagamento = lambda id: "recibo de pagamento impresso" if transacoes["status"][transacoes["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

retornar_recibo_pagamento = lambda id: "recibo de pagamento retornado" if transacoes["status"][transacoes["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

completar_transacao = lambda id: [transacoes["status"].__setitem__(transacoes["id"].index(id), "transação concluída") if transacoes["status"][transacoes["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"] and print("Transação Concluida")

fechar_transacao = lambda id: transacoes["status"][transacoes["id"].index(id)] == "transação fechada" if transacoes["status"][transacoes["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"

cancelar_transacao = lambda id: transacoes["status"][transacoes["id"].index(id)] == "transação cancelada" if transacoes["status"][transacoes["id"].index(id)] == "pagamento não aprovado" else "erro"


conta_atualizada = atualizar_conta_corrente(1, 1500)
print(conta_atualizada)  # Saída: {1: 1500, 2: 500, 3: 1200}

# # criar uma transação de dinheiro
# criar_transacao(1, "dinheiro")
# print(transacoes)

# # receber dinheiro para a transação
# receber_dinheiro(1)
# print(transacoes)  # saida: {'id': [1], 'tipo': ['dinheiro'], 'status': ['dinheiro recebido']}

# # imprimir recibo de pagamento
# print(imprimir_recibo_pagamento(1))  # saida: recibo de pagamento impresso

# # retornar recibo de pagamento
# print(retornar_recibo_pagamento(1))  # saida: recibo de pagamento retornado

# # completar a transação
# completar_transacao(1)
# print(transacoes)  # saida: {'id': [1], 'tipo': ['dinheiro'], 'status': ['transação concluída']}

