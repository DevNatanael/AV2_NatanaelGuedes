# dicionários para armazenar detalhes da transação
transacoes = lambda id, tipo, status: {"id": [id], "tipo": [tipo], "status": [status]}
detalhes_conta = lambda id, detalhes: {"id": [id], "detalhes": [detalhes]}
detalhes_banco = lambda id, detalhes: {"id": [id], "detalhes": [detalhes]}

# dicionários para armazenar detalhes da conta do usuário
contas_correntes = lambda id, saldo: {"id": [id], "saldo": [saldo]}

usuarios = lambda id,senha :{"id": [id], "senha": [senha]}

# funções lambda
criar_transacao = lambda id, tipo: transacoes(id, tipo, "criada")

receber_dinheiro = lambda id,novaTransacao: novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "dinheiro recebido") if id in novaTransacao["id"] else print("Transação não encontrada")

solicitar_detalhes_conta = lambda id, detalhes, novaTransacao: [detalhes_conta["detalhes"].append(detalhes) if novaTransacao["tipo"][novaTransacao["id"].index(id)] == "credito" else "erro"] and print("Solicitando detalhes de crédito da conta")

solicitar_pagamento_banco = lambda id, novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento solicitado"), print("Solicitando pagamento do banco")) if novaTransacao["tipo"][novaTransacao["id"].index(id)] == "credito" else "erro"

confirmar_pagamento_banco = lambda id, aprovado, novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento aprovado"), print("Confirme a aprovação do pagamento do banco")) if aprovado else (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento não aprovado"), print("Pagamento não aprovado pelo banco"))

fornecer_detalhes_deposito_banco = lambda id, detalhes,novaTransacao: (detalhes_banco["id"].append(id), detalhes_banco["detalhes"].append(detalhes), print("Forneça detalhes de depósito bancário")) if novaTransacao["status"][novaTransacao["id"].index(id)] == "pagamento aprovado" else "erro"

transferir_fundos = lambda id,novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "fundos transferidos"), print("Fundos transferidos")) if novaTransacao["status"][novaTransacao["id"].index(id)] == "pagamento aprovado" else "erro"

imprimir_recibo_pagamento = lambda id, novaTransacao: "recibo de pagamento impresso" if novaTransacao["status"][novaTransacao["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

retornar_recibo_pagamento = lambda id,novaTransacao: "recibo de pagamento retornado" if novaTransacao["status"][novaTransacao["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

completar_transacao = lambda id,novaTransacao: [novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "transação concluída") if novaTransacao["status"][novaTransacao["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"] and print("Transação Concluida")

fechar_transacao = lambda id,novaTransacao: novaTransacao["status"][novaTransacao["id"].index(id)] == "transação fechada" if novaTransacao["status"][novaTransacao["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"

cancelar_transacao = lambda id,novaTransacao: novaTransacao["status"][novaTransacao["id"].index(id)] == "transação cancelada" if novaTransacao["status"][novaTransacao["id"].index(id)] == "pagamento não aprovado" else "erro"

criar_conta_corrente = lambda id: contas_correntes(id, 0)

atualizar_conta_corrente = lambda novaConta,id, valor: [novaConta["saldo"].__setitem__(novaConta["id"].index(id), novaConta["saldo"][novaConta["id"].index(id)] + valor) if id in novaConta["id"] else "erro"] and print("Dinheiro recebido")

#criar usuario
print("Criando usuario")
novoUsuario = usuarios(1,"senha123")
print(novoUsuario)

# criar uma conta
print("Criando conta")
novaConta = criar_conta_corrente(1)
novaConta2 = criar_conta_corrente(2)

print(novaConta)

# criar uma transação de dinheiro
print("Criando transação")
novaTransacao = criar_transacao(1, "dinheiro")
print(novaTransacao)

# atualizar a conta corrente do usuário
atualizar_conta_corrente(novaConta,1, 100)
print(novaConta)

# receber dinheiro para a transação
print("Recebendo dinheiro")
receber_dinheiro(1, novaTransacao)
print(novaTransacao)

# imprimir recibo de pagamento
print(imprimir_recibo_pagamento(1,novaTransacao))

# retornar recibo de pagamento
print(retornar_recibo_pagamento(1,novaTransacao))

# completar a transação
completar_transacao(1,novaTransacao)
print(novaTransacao)

