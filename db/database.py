from calendar import c
from math import e
import re
from sqlite3 import Cursor
import mysql.connector

class Data_base:
    def __init__(self, host="localhost", user="root", password="123456", database="cadastro_escola"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        print('tentado conectar o banco de dados')
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conectado ao banco de dados com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def create_table_new_user(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        nome VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        senha VARCHAR(50) NOT NULL, 
        admin BOOLEAN
        )""")
        self.connection.commit() 

    def create_table_new_student(self):
        cursor = self.connection.cursor()
        cursor.execute ("""CREATE TABLE IF NOT EXISTS alunos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        cpf VARCHAR(14) NOT NULL UNIQUE,
        rg VARCHAR(12) NOT NULL,
        estado_civil ENUM('solteiro', 'casado', 'viuvo') NOT NULL,
        endereco TEXT NOT NULL,
        sexo ENUM('masculino', 'feminino') NOT NULL,
        nascimento DATE NOT NULL,
        telefone1 VARCHAR(15) NOT NULL,
        telefone2 VARCHAR(15)
        )""")

        print("Tabela criada com sucesso ou tabela já existente")
        self.connection.commit()     

    def register_new_student(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO alunos (nome, email, cpf, rg, estado_civil, endereco, sexo, nascimento, telefone1, telefone2)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
            return ("ok")

        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def register_new_user(self, fullDataSet):
        """ Registra um novo usuário no banco de dados. """
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO usuarios (nome, email, senha, admin) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
            return ("ok")
            
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
    
    def pega_dados(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def select_all_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as e:
            print(f"Erro ao selecionar todos os usuários: {e}")    

    def delete_user(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))

            self.connection.commit()

            return "Cadastro de usuarios exlcuido com sucesso!"

        except mysql.connector.Error as e:
            print(f"Erro ao excluir usuário: {e}")    

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        try:
            if self.connection:
                self.connection.close()
                print("Conexão fechada com sucesso!")
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

# Exemplo de uso
db = Data_base()
db.connect()
db.create_table_new_user()
db.create_table_new_student()
db.close_connection()