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
        email VARCHAR(50) NOT NULL UNIQUE, 
        senha VARCHAR(50) NOT NULL, 
        admin BOOLEAN NOT NULL DEFAULT FALSE
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
        estado_civil ENUM('Solteiro', 'Casado', 'Viuvo') NOT NULL,
        endereco TEXT NOT NULL,
        sexo ENUM('Masculino', 'Feminino') NOT NULL,
        nascimento DATE NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        periodo ENUM('Diurno','Noturno') NOT NULL,
        turma ENUM('Ads', 'Data-science', 'Machine-learning', 'Software-engineer') NOT NULL,
        isAtivo TINYINT(1) DEFAULT 1
        )""")

        print("Tabela criada com sucesso ou tabela já existente")   
        self.connection.commit() 

    def register_new_student(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO alunos (nome, email, cpf, rg, estado_civil, endereco, sexo, nascimento, telefone, periodo, turma, isAtivo)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
            return ("ok")

        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:  
                print("Erro: E-mail ou CPF já cadastrado!")
                return "duplicate_entry"
            else:
                print(f"Erro ao cadastrar usuário: {e}")
                return False

    def create_table_new_teacher(self):
        cursor = self.connection.cursor()
        cursor.execute ("""CREATE TABLE IF NOT EXISTS professores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        cpf VARCHAR(14) NOT NULL UNIQUE,
        rg VARCHAR(12) NOT NULL,
        estado_civil ENUM('Solteiro', 'Casado', 'Viuvo') NOT NULL,
        endereco TEXT NOT NULL,
        sexo ENUM('Masculino', 'Feminino') NOT NULL,
        nascimento DATE NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        periodo ENUM('Diurno','Noturno') NOT NULL,
        turma ENUM('Ads', 'Data-science', 'Machine-learning', 'Software-engineer') NOT NULL,
        isAtivo TINYINT(1) DEFAULT 1
        )""")

        print("Tabela criada com sucesso ou tabela já existente")
        self.connection.commit()     

    def register_new_teacher(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO professores (nome, email, cpf, rg, estado_civil, endereco, sexo, nascimento, telefone, periodo, turma, isAtivo)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
            return ("ok")

        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def register_new_user(self, fullDataSet):
        """ Registra um novo usuário no banco de dados. """
        try:
            cursor = self.connection.cursor()

            verifica_sql = "SELECT 1 FROM usuarios WHERE email = %s"
            cursor.execute(verifica_sql, (fullDataSet[1],)) 

            if cursor.fetchone():
                return False 

            sql = "INSERT INTO usuarios (nome, email, senha, admin) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
           
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
    
    def pega_dados(self, email, senha ):
        cursor = self.connection.cursor()
        querry = ("SELECT * FROM usuarios where email=%s AND senha = %s")
        cursor.execute(querry, (email, senha))

        return cursor.fetchone()

    def confereEmail(self, email_digitado):
        cursor = None
        try:
            cursor = self.connection.cursor()
            querry = ("SELECT email FROM usuarios WHERE email = %s")
            cursor.execute(querry, (email_digitado,))

            resultado = cursor.fetchone()
            return resultado is not None

        except mysql.connector.Error as e:
            print(f"Erro no banco: {e}")
            return "Erro ao verificar o e-mail no banco"
            
        finally:
            if cursor:
                cursor.close()
            
    def alter_password(self, nova_senha, email):
        cursor = None
        try:
            cursor = self.connection.cursor()
            querry = ("UPDATE usuarios SET senha = %s WHERE email = %s")
            cursor.execute(querry, (nova_senha, email))
            self.connection.commit()
            return True 
        except mysql.connector.Error as e:
            return False  
        finally:
            if cursor:
             cursor.close()    

    def select_all_users(self):
        try:
            db.connect()
            cursor = db.connection.cursor()

            query = """
                SELECT id, nome, email, cpf, periodo, turma
                FROM alunos
                UNION ALL
                SELECT id, nome, email, cpf, periodo, turma 
                FROM professores;
            """
            cursor.execute(query)

            dados = cursor.fetchall()
            return dados

        except mysql.connector.Error as e:
            print(f"Erro ao buscar dados: {e}")
            return "Erro ao buscar dados no banco"

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
db.create_table_new_teacher()
db.close_connection()