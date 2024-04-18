import time

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
# função para testar a igualdade
testar_igualdade = lambda x, y: x if x == y else print(f"Erro: {x} != {y}")


# teste unitário 1: Testar uma transação de dinheiro
teste_transacao_dinheiro = lambda: (novaTransacao := criar_transacao(1, "dinheiro"), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['criada']}), receber_dinheiro(1,novaTransacao), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['dinheiro recebido']}), completar_transacao(1,novaTransacao), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['transação concluída']}))
teste_transacao_dinheiro()

# # teste unitário 2: Testar uma transação de crédito bem-sucedida
# teste_transacao_credito_bem_sucedida = lambda: (criar_transacao(2, "credito"), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['criada']}), solicitar_detalhes_conta(2, "1234-5678-9012-3456"), testar_igualdade(detalhes_conta, {'id': [2], 'detalhes': ['1234-5678-9012-3456']}), solicitar_pagamento_banco(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['pagamento solicitado']}), confirmar_pagamento_banco(2, True), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['pagamento aprovado']}), fornecer_detalhes_deposito_banco(2, "Banco XYZ, Conta: 123456"), testar_igualdade(detalhes_banco, {'id': [2], 'detalhes': ['Banco XYZ, Conta: 123456']}), transferir_fundos(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['fundos transferidos']}), completar_transacao(2), testar_igualdade(transacoes, {'id': [2], 'tipo': ['credito'], 'status': ['transação concluída']}))
# teste_transacao_credito_bem_sucedida()

# # Teste unitário 3: Testar uma transação de crédito mal-sucedida
# teste_transacao_credito_mal_sucedida = lambda: (criar_transacao(3, "credito"), testar_igualdade(transacoes, {'id': [3], 'tipo': ['credito'], 'status': ['criada']}), solicitar_detalhes_conta(3, "1234-5678-9012-3456"), testar_igualdade(detalhes_conta, {'id': [3], 'detalhes': ['1234-5678-9012-3456']}), solicitar_pagamento_banco(3), testar_igualdade(transacoes, {'id': [3], 'tipo': ['credito'], 'status': ['pagamento solicitado']}), confirmar_pagamento_banco(3, False), testar_igualdade(transacoes, {'id': [3], 'tipo': ['credito'], 'status': ['pagamento não aprovado']}))
# teste_transacao_credito_mal_sucedida()

# # Teste de stress: Criar um grande número de transações e medir o tempo que leva para processá-las
# teste_stress = lambda: (
#     # Limpar as listas de transações anteriores
#     transacoes["id"].clear(),
#     transacoes["tipo"].clear(),
#     transacoes["status"].clear(),
#     # Iniciar o tempo
#     start_time := time.time(),
#     # Criar 50 mil transações de dinheiro
#     [(criar_transacao(i, "dinheiro"), receber_dinheiro(i), completar_transacao(i)) for i in range(50000)],
#     # Parar o tempo
#     end_time := time.time(),
#     # Imprimir o tempo que levou para processar 1 milhão de transações
#     print(f"Tempo para processar 50 mil transações: {end_time - start_time} segundos")
# )
# teste_stress()

