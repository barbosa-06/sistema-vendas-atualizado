from database import conectar

conexao, cursor = conectar()

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(50) NOT NULL,
        telefone VARCHAR(20) NOT NULL)""") 

conexao.commit()


