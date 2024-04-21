
# PROGRAMA ESCOLHIDO FOI O DA QUESTÃO 3

from flask import Flask, request, jsonify
import bcrypt
import mysql.connector

app = Flask(__name__)

conectar = lambda: mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="av2Python"
)

# criar tabelas
criar_tabelas = lambda conexao, tabelas: [conexao.cursor().execute(tabela) for tabela in tabelas] and print("tabelas criadas")

# inserir registros
inserir = lambda conexao, tabela, valores: (conexao.cursor().execute(f"INSERT INTO {tabela} VALUES ({', '.join(['%s'] * len(valores))})", valores), conexao.commit()) and print("Dado adicionado")

# remover registros
remover = lambda conexao, tabela, condicao: (conexao.cursor().execute(f"DELETE FROM {tabela} WHERE {condicao}"), conexao.commit()) and print("Dado removido")

# consultar registros
consultar = lambda conexao, tabela, condicao: (cursor := conexao.cursor(), cursor.execute(f"SELECT * FROM {tabela} WHERE {condicao}"), cursor.fetchall())[2]

# função para criptografar senha
criptografar_senha = lambda senha: bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

@app.route('/criar_tabelas', methods=['POST'])
def criar_tabelas_route():
    tabelas = request.json.get('tabelas')
    if not tabelas:
        return jsonify({'error': 'Nenhuma tabela fornecida'}), 400
    conexao = conectar()
    criar_tabelas(conexao, tabelas)
    return jsonify({'message': 'Tabelas criadas com sucesso!'}), 200

@app.route('/inserir', methods=['POST'])
def inserir_registro():
    dados = request.json
    tabela = dados.get('tabela')
    valores = dados.get('valores')
    if not tabela or not valores:
        return jsonify({'error': 'Tabela ou valores não fornecidos'}), 400
    conexao = conectar()
    inserir(conexao, tabela, valores)
    return jsonify({'message': 'Registro inserido com sucesso!'}), 200

@app.route('/remover', methods=['DELETE'])
def remover_registro():
    dados = request.json
    tabela = dados.get('tabela')
    condicao = dados.get('condicao')
    if not tabela or not condicao:
        return jsonify({'error': 'Tabela ou condição não fornecidos'}), 400
    conexao = conectar()
    remover(conexao, tabela, condicao)
    return jsonify({'message': 'Registro removido com sucesso!'}), 200

@app.route('/consultar', methods=['GET'])
def consultar_registro():
    tabela = request.args.get('tabela')
    condicao = request.args.get('condicao')
    if not tabela or not condicao:
        return jsonify({'error': 'Tabela ou condição não fornecidos'}), 400
    conexao = conectar()
    result = consultar(conexao, tabela, condicao)
    return jsonify({'result': result}), 200

@app.route('/criptografar_senha', methods=['POST'])
def criptografar_senha_route():
    senha = request.json.get('senha')
    if not senha:
        return jsonify({'error': 'Nenhuma senha fornecida'}), 400
    senha_criptografada = criptografar_senha(senha)
    return jsonify({'senha_criptografada': senha_criptografada}), 200

if __name__ == '__main__':
    app.run(debug=True)
