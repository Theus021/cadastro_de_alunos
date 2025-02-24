import mysql.connector
from mysql.connector import Error

class MySQLDB:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456",
                database=""
            )
            self.cursor = self.db.cursor()

            self.cursor.execute("CREATE DATABASE IF NOT EXISTS Cadastro_escola")
            print("Banco de dados criado ou já existente.")

            self.cursor.execute("USE Cadastro_escola")
            print("Banco de dados selecionado com sucesso!")

        except Error as e:
            print("Erro ao conectar ou ao criar banco de dados: ", e)

    def criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS funcionarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            admin BOOLEAN NOT NULL
        )""")
        print("Tabela criada com sucesso!")

    def close(self):
        if self.db:
            self.db.close()
            print("Conexão com o MySQL fechada.")

if __name__ == "__main__":
    db = MySQLDB()
    db.criar_tabela()
    db.close()