from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telas.tela_login import Ui_Dialog_login
from modulos.registerM import open_cadastrar
from db.database import Data_base

class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog_login()
        self.ui.setupUi(self)
        self.ui.entrar_button.clicked.connect(self.login)
        self.ui.cadastrar_button.clicked.connect(open_cadastrar)

    def login(self):
        user = self.ui.email_input.text()  # Certifique-se de que o nome do campo de entrada está correto
        password = self.ui.senha_input.text()  # Certifique-se de que o nome do campo de entrada está correto

        if user.strip() == "" or password.strip() == "":
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
        else:
            db = Data_base()  # Criando a instância do banco de dados
            db.connect()  # Conectando ao banco
            dados = db.pega_dados("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (user, password))
            print(f"Dados retornados do banco: {dados}")
            if dados:
                QMessageBox.information(self, "Login", "Login realizado com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Email ou senha inválidos")
            db.close_connection()  # Fechando a conexão com o banco

db = Data_base()  # Instanciando o banco de dados
db.connect()  # Conectando ao banco de dados

app = QApplication(sys.argv)
window = login()
window.show()
sys.exit(app.exec_())
