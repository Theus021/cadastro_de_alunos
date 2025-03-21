from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telas.tela_login import Ui_Dialog_login
from modulos.registerUser import open_cadastrar
from modulos.pagina_inicial import telaPrincipal
from modulos.recuperacao import request_password
from db.database import Data_base


class Login(QDialog):  # Nome da classe começa com maiúscula por convenção
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_login()
        self.ui.setupUi(self)
        
        self.ui.entrar_button.clicked.connect(self.login)
        self.ui.cadastrar_button.clicked.connect(open_cadastrar)
        self.ui.pushButton.clicked.connect(request_password)

        
    def login(self):
        user = self.ui.email_input.text().strip()
        password = self.ui.senha_input.text().strip()

        if not user or not password:
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return

        db = Data_base()
        db.connect()
        email_check = db.verificaEmail(user)

        if not email_check:
            QMessageBox.information(self, "Erro", "E-mail ou senha inválida")
            db.close_connection()
            return

        pass_check = db.confere_dados_user(user, password)

        if not pass_check:
            QMessageBox.information(self, "Erro", "Senha inválida")
            db.close_connection()
            return    

        else:
            QMessageBox.information(self, "Login realizado!", "Login realizado com sucesso!")
            self.close()  
            self.window = telaPrincipal()  
            self.window.show()
       

        db.close_connection()

app = QApplication(sys.argv)
window = Login()  
window.show()
sys.exit(app.exec_())
