import time

# dicionários para armazenar detalhes da transação
transacoes = lambda id, tipo, status: {"id": [id], "tipo": [tipo], "status": [status]}

# dicionários para armazenar detalhes da conta do usuário
contas_correntes = lambda id, saldo: {"id": [id], "saldo": [saldo]}

usuarios = lambda id,senha :{"id": [id], "senha": [senha]}

# funções lambda
criar_transacao = lambda id, tipo: transacoes(id, tipo, "criada")

receber_dinheiro = lambda id,novaTransacao: novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "dinheiro recebido") if id in novaTransacao["id"] else print("Transação não encontrada")

solicitar_detalhes_conta = lambda novaConta: print('Detalhes Conta: ' + str(novaConta))

solicitar_pagamento_banco = lambda id, novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento solicitado"), print("Solicitando pagamento do banco")) if novaTransacao["tipo"][novaTransacao["id"].index(id)] == "credito" else "erro"

confirmar_pagamento_banco = lambda id, aprovado, novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento aprovado"), print("Confirmando a aprovação do pagamento do banco")) if aprovado else (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "pagamento não aprovado"), print("Pagamento não aprovado pelo banco"))

fornecer_detalhes_deposito_banco = lambda deposito: print('Detalhes deposito: ' + str(deposito))

transferir_fundos = lambda id,novaTransacao: (novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "fundos transferidos"), print("Transferindo fundos")) if novaTransacao["status"][novaTransacao["id"].index(id)] == "pagamento aprovado" else "erro"

imprimir_recibo_pagamento = lambda id, novaTransacao: "recibo de pagamento impresso" if novaTransacao["status"][novaTransacao["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

retornar_recibo_pagamento = lambda id,novaTransacao: "recibo de pagamento retornado" if novaTransacao["status"][novaTransacao["id"].index(id)] in ["fundos transferidos", "dinheiro recebido"] else "erro"

completar_transacao = lambda id,novaTransacao: [novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "transação concluída") if novaTransacao["status"][novaTransacao["id"].index(id)] in ["dinheiro recebido", "fundos transferidos"] else "erro"] and print("Transação Concluida")

fechar_transacao = lambda id,novaTransacao: [novaTransacao["status"].__setitem__(novaTransacao["id"].index(id), "transação fechada") if novaTransacao["status"][novaTransacao["id"].index(id)] in ["transação concluída"] else "erro"] and print("Transação Fechada")

cancelar_transacao = lambda id,novaTransacao: novaTransacao["status"][novaTransacao["id"].index(id)] == "transação cancelada" if novaTransacao["status"][novaTransacao["id"].index(id)] == "pagamento não aprovado" else "erro"

criar_conta_corrente = lambda id: contas_correntes(id, 0)

atualizar_conta_corrente = lambda novaConta,id, valor: [novaConta["saldo"].__setitem__(novaConta["id"].index(id), novaConta["saldo"][novaConta["id"].index(id)] + valor) if id in novaConta["id"] else "erro"] and print("Dinheiro recebido")

# função para testar a igualdade
testar_igualdade = lambda x, y: x if x == y else print(f"Erro: {x} != {y}")


# teste unitário 1: Testar uma transação de dinheiro
print("Testando uma transação de dinheiro")
teste_transacao_dinheiro = lambda: (novaTransacao := criar_transacao(1, "dinheiro"), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['criada']}), receber_dinheiro(1,novaTransacao), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['dinheiro recebido']}), completar_transacao(1,novaTransacao), testar_igualdade(novaTransacao, {'id': [1], 'tipo': ['dinheiro'], 'status': ['transação concluída']}))
teste_transacao_dinheiro()

print("-----------")

#teste unitário 2: Testar uma transação de crédito
print("Testando uma transação de crédio")
teste_transacao_credito = lambda: (novaTransacao2 := criar_transacao(2, "credito"), testar_igualdade(novaTransacao2, {'id': [2], 'tipo': ['credito'], 'status': ['criada']}), receber_dinheiro(2,novaTransacao2), testar_igualdade(novaTransacao2, {'id': [2], 'tipo': ['credito'], 'status': ['dinheiro recebido']}), completar_transacao(2,novaTransacao2), testar_igualdade(novaTransacao2, {'id': [2], 'tipo': ['credito'], 'status': ['transação concluída']}))
teste_transacao_credito()

print("-----------")

print("Testando uma transação de crédio mal-sucedida")
# Teste unitário 3: Testar uma transação de crédito mal-sucedida
teste_transacao_credito_mal_sucedida = lambda: (novaTransacao3 := criar_transacao(3, "credito"), testar_igualdade(novaTransacao3, {'id': [3], 'tipo': ['credito'], 'status': ['criada']}), solicitar_pagamento_banco(3,novaTransacao3), testar_igualdade(novaTransacao3, {'id': [3], 'tipo': ['credito'], 'status': ['pagamento solicitado']}), confirmar_pagamento_banco(3, False,novaTransacao3), testar_igualdade(novaTransacao3, {'id': [3], 'tipo': ['credito'], 'status': ['pagamento não aprovado']}))
teste_transacao_credito_mal_sucedida()

print("-----------")

#--- ATENÇÃO : para fazer o teste de stress por favor descomente o código abaixo:
# Teste de stress: Criar um grande número de transações e medir o tempo que leva para processá-las
# teste_stress = lambda: (
#     # Iniciar o tempo
#     start_time := time.time(),
#     # Criar 50 mil transações de dinheiro
#     [(novaTransacao5 := criar_transacao(i, "dinheiro"), receber_dinheiro(i,novaTransacao5), completar_transacao(i,novaTransacao5)) for i in range(1,50001)],
#     # Parar o tempo
#     end_time := time.time(),
#     # Imprimir o tempo que levou para processar 1 milhão de transações
#     print(f"Tempo para processar 50 mil transações: {end_time - start_time} segundos")
# )
# teste_stress()

