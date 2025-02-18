import mysql.connector

def conectar():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meu_banco"
    )

def adiconar_user(login,senha):
    conexao=conectar()
    cursor=conexao.cursor()
    sql="INSERT INTO usuarios (email, senha_hash) VALUES (%s, SHA(%s,256))"
    valores=(login, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
