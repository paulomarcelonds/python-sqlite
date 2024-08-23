import sqlite3

#criar o banco banco de dados e conexão
con = sqlite3.connect('cinema.db')

#criar um objeto cursor
cur = con.cursor()

#criar uma tabela
#cur.execute('CREATE TABLE filme(titulo, ano, duracao)')

#verificar se a tabela foi criada
res = cur.execute('SELECT * FROM sqlite_master')
res.fetchone()