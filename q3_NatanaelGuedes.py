import mysql.connector

conectar = lambda: mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="av2Python"
)

# criar tabelas
criar_tabelas = lambda conexao, tabelas: [conexao.cursor().execute(tabela) for tabela in tabelas] and print("tabelas criadas")

declaracoes_tabelas = [
    """
    CREATE TABLE IF NOT EXISTS USERS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        country VARCHAR(255),
        id_console INT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS VIDEOGAMES (
        id_console INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        id_company INT,
        release_date DATE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS GAMES (
        id_game INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        genre VARCHAR(255),
        release_date DATE,
        id_console INT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS COMPANY (
        id_company INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        country VARCHAR(255)
    )
    """
]

# inserir registros
inserir = lambda conexao, tabela, valores: (conexao.cursor().execute(f"INSERT INTO {tabela} VALUES ({', '.join(['%s'] * len(valores))})", valores), conexao.commit()) and print("Dado adicionado")

# remover registros
remover = lambda conexao, tabela, condicao: (conexao.cursor().execute(f"DELETE FROM {tabela} WHERE {condicao}"), conexao.commit()) and print("Dado removido")

# consultar registros
consultar = lambda conexao, tabela, condicao: (cursor := conexao.cursor(), cursor.execute(f"SELECT * FROM {tabela} WHERE {condicao}"), cursor.fetchall())[2]

conexao = conectar()

# create tables
criar_tabelas(conexao, declaracoes_tabelas)

# insert
inserir(conexao, "USERS", (None, 'Pedro', 'BRA', 3))

# delete
remover(conexao, "USERS", "id = 5")

# select
result = consultar(conexao, "USERS", "country = 'USA'")
print(result)
