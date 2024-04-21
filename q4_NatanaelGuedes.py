
# função para gerar a parte INNER JOIN da consulta SQL
gerar_inner_join = lambda tabela1, tabela2, tabela3, condicao1, condicao2: f"{tabela1} INNER JOIN {tabela2} ON {condicao1} INNER JOIN {tabela3} ON {condicao2}"

# função para gerar a parte SELECT da consulta SQL
gerar_select = lambda campos, inner_join, condicao: f"SELECT {', '.join(campos)} FROM {inner_join} WHERE {condicao}"

inner_join = gerar_inner_join("GAMES", "VIDEOGAMES", "COMPANY", "GAMES.id_console = VIDEOGAMES.id_console", "VIDEOGAMES.id_company = COMPANY.id_company")
select = gerar_select(["GAMES.title", "COMPANY.name"], inner_join, "GAMES.id_console = VIDEOGAMES.id_console AND VIDEOGAMES.id_company = COMPANY.id_company")

# consulta SQL completa
consulta_sql = f"{select}"
print(consulta_sql)
