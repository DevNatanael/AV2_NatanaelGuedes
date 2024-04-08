# dicionários para armazenar detalhes da transação
transacoes = {"id": [], "tipo": [], "status": []}
detalhes_conta = {"id": [], "detalhes": []}
detalhes_banco = {"id": [], "detalhes": []}

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

# função para testar a igualdade
testar_igualdade = lambda x, y: x if x == y else print(f"Erro: {x} != {y}")

# teste unitário 1: Testar uma transação de dinheiro
teste_transacao_dinheiro = lambda: (criar_transacao(1, "dinheiro"), testar_igualdade(transacoes, {'id': [1], 'tipo': ['dinheiro'], 'status': ['criada']}), receber_dinheiro(1), testar_igualdade(transacoes, {'id': [1], 'tipo': ['dinheiro'], 'status': ['dinheiro recebido']}), completar_transacao(1), testar_igualdade(transacoes, {'id': [1], 'tipo': ['dinheiro'], 'status': ['transação concluída']}))
teste_transacao_dinheiro()

# teste unitário 2: Testar uma transação de crédito bem-sucedida
teste_transacao_credito_bem_sucedida = lambda: (criar_transacao(2, "credito"), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['criada']}), solicitar_detalhes_conta(2, "1234-5678-9012-3456"), testar_igualdade(detalhes_conta, {'id': [2], 'detalhes': ['1234-5678-9012-3456']}), solicitar_pagamento_banco(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['pagamento solicitado']}), confirmar_pagamento_banco(2, True), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['pagamento aprovado']}), fornecer_detalhes_deposito_banco(2, "Banco XYZ, Conta: 123456"), testar_igualdade(detalhes_banco, {'id': [2], 'detalhes': ['Banco XYZ, Conta: 123456']}), transferir_fundos(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['fundos transferidos']}), completar_transacao(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['transação concluída']}))
teste_transacao_credito_bem_sucedida()
