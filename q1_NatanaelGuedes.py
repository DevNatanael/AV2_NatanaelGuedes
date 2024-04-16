# dicionários para armazenar detalhes da transação
transacoes = lambda id, tipo, status: {"id": [id], "tipo": [tipo], "status": [status]}
detalhes_conta = lambda id, detalhes: {"id": [id], "detalhes": [detalhes]}
detalhes_banco = lambda id, detalhes: {"id": [id], "detalhes": [detalhes]}

# dicionários para armazenar detalhes do usuário
contas_correntes = lambda id, saldo: {"id": [id], "saldo": [saldo]}
senhas = lambda id, senha: {"id": [id], "senha": [senha]}

# funções lambda
criar_transacao = lambda id, tipo: transacoes(id, tipo, "criada")

receber_dinheiro = lambda id,novaTransacao: novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "dinheiro recebido") if id in novaTransacao["id"] else print("Transação não encontrada")

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

criar_usuario = lambda id, senha: (senhas["id"].append(id), senhas["senha"].append(senha), contas_correntes["id"].append(id), contas_correntes["saldo"].append(0), print("Usuário criado"))

atualizar_conta_corrente = lambda id, valor: [contas_correntes["saldo"].__setitem__(contas_correntes["id"].index(id), contas_correntes["saldo"][contas_correntes["id"].index(id)] + valor) if id in contas_correntes["id"] else "erro"] and print("Conta corrente atualizada")


# # criar um usuário
# criar_usuario(1, "senha123")
# print(senhas)
# print(contas_correntes)

# criar uma transação de dinheiro
print("Criando transação")
novaTransacao = criar_transacao(1, "dinheiro")
print(novaTransacao)

# # atualizar a conta corrente do usuário
# atualizar_conta_corrente(1, 100)
# print(contas_correntes)

# receber dinheiro para a transação
receber_dinheiro(1, novaTransacao)
print(novaTransacao)

# # imprimir recibo de pagamento
# print(imprimir_recibo_pagamento(1))

# # retornar recibo de pagamento
# print(retornar_recibo_pagamento(1))

# # completar a transação
# completar_transacao(1)
# print(transacoes)

