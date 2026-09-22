import psycopg

def conectar():
    conexao = psycopg.connect(
        host= "localhost",
        dbname= "sistema_vendas",
        user= "postgres",
        password= "1404",
        port=5432
    )

    cursor = conexao.cursor()
    return conexao, cursor

