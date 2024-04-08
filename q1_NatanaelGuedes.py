# dicionários para armazenar detalhes da transação
transacoes = {"id": [], "tipo": [], "status": []}
detalhes_conta = {"id": [], "detalhes": []}
detalhes_banco = {"id": [], "detalhes": []}

# funções lambda
criar_transacao = lambda id, tipo: [transacoes[chave].append(valor) for chave, valor in {"id": id, "tipo": tipo, "status": "criada"}.items()] and (detalhes_conta["id"].append(id) and detalhes_conta["detalhes"].append(None) if tipo == "credito" else None) and print("Create Transaction")

receber_dinheiro = lambda id: [transacoes["status"].__setitem__(transacoes["id"].index(id), "dinheiro recebido") if transacoes["tipo"][transacoes["id"].index(id)] == "dinheiro" else "erro"] and print("Receive Cash")

solicitar_detalhes_conta = lambda id, detalhes: [detalhes_conta["detalhes"].append(detalhes) if transacoes["tipo"][transacoes["id"].index(id)] == "credito" else "erro"] and print("Request Account Credit Details")

solicitar_pagamento_banco = lambda id: transacoes["status"][transacoes["id"].index(id)] == "pagamento solicitado" if transacoes["tipo"][transacoes["id"].index(id)] == "credito" else "erro"

confirmar_pagamento_banco = lambda id, aprovado: transacoes["status"][transacoes["id"].index(id)] == "pagamento aprovado" if aprovado else "pagamento não aprovado"

fornecer_detalhes_deposito_banco = lambda id, detalhes: detalhes_banco["detalhes"][detalhes_banco["id"].index(id)] == detalhes if transacoes["status"][transacoes["id"].index(id)] == "pagamento aprovado" else "erro"

transferir_fundos = lambda id: transacoes["status"][transacoes["id"].index(id)] == "fundos transferidos" if transacoes["status"][transacoes["id"].index(id)] == "pagamento aprovado" else "erro"

imprimir_recibo_pagamento = lambda id: "recibo de pagamento impresso" if transacoes["status"][transacoes["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

retornar_recibo_pagamento = lambda id: "recibo de pagamento retornado" if transacoes["status"][transacoes["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

completar_transacao = lambda id: [transacoes["status"].__setitem__(transacoes["id"].index(id), "transação concluída") if transacoes["status"][transacoes["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"] and print("Complete Transaction")

fechar_transacao = lambda id: transacoes["status"][transacoes["id"].index(id)] == "transação fechada" if transacoes["status"][transacoes["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"

cancelar_transacao = lambda id: transacoes["status"][transacoes["id"].index(id)] == "transação cancelada" if transacoes["status"][transacoes["id"].index(id)] == "pagamento não aprovado" else "erro"

# criar uma transação de dinheiro
criar_transacao(1, "dinheiro")
print(transacoes)  # saida: {'id': [1], 'tipo': ['dinheiro'], 'status': ['criada']}

# Receber dinheiro para a transação
receber_dinheiro(1)
print(transacoes)  # saida: {'id': [1], 'tipo': ['dinheiro'], 'status': ['dinheiro recebido']}

# Imprimir recibo de pagamento
print(imprimir_recibo_pagamento(1))  # saida: recibo de pagamento impresso

# Retornar recibo de pagamento
print(retornar_recibo_pagamento(1))  # saida: recibo de pagamento retornado

# Completar a transação
completar_transacao(1)
print(transacoes)  # saida: {'id': [1], 'tipo': ['dinheiro'], 'status': ['transação concluída']}

print("-----------")

# Criar uma transação de crédito
criar_transacao(2, "credito")
print(transacoes)  # saida: {'id': [1, 2], 'tipo': ['dinheiro', 'credito'], 'status': ['transação concluída', 'criada']}

# Solicitar detalhes da conta
solicitar_detalhes_conta(2, "1234-5678-9012-3456")
print(detalhes_conta)  # saida: {'id': [2], 'detalhes': ['1234-5678-9012-3456']}

# Solicitar pagamento do banco
solicitar_pagamento_banco(2)
print(transacoes)  # saida: {'id': [1, 2], 'tipo': ['dinheiro', 'credito'], 'status': ['transação concluída', 'pagamento solicitado']}

# Confirmar aprovação do pagamento pelo banco
confirmar_pagamento_banco(2, True)
print(transacoes)  # saida: {'id': [1, 2], 'tipo': ['dinheiro', 'credito'], 'status': ['transação concluída', 'pagamento aprovado']}

# Fornecer detalhes de depósito do banco
fornecer_detalhes_deposito_banco(2, "Banco XYZ, Conta: 123456")
print(detalhes_banco)  # saida: {'id': [2], 'detalhes': ['Banco XYZ, Conta: 123456']}

# Transferir fundos
transferir_fundos(2)
print(transacoes)  # saida: {'id': [1, 2], 'tipo': ['dinheiro', 'credito'], 'status': ['transação concluída', 'fundos transferidos']}

# Imprimir recibo de pagamento
print(imprimir_recibo_pagamento(2))  # saida: recibo de pagamento impresso

# Retornar recibo de pagamento
print(retornar_recibo_pagamento(2))  # saida: recibo de pagamento retornado

# Completar a transação
completar_transacao(2)
print(transacoes)  # saida: {'id': [1, 2], 'tipo': ['dinheiro', 'credito'], 'status': ['transação concluída', 'transação concluída']}
