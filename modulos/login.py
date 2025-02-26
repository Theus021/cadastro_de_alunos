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
        self.ui.entrar_button.clicked.connect(self.login)  # Certifique-se de que o nome do botão está correto
        self.ui.cadastrar_button.clicked.connect(open_cadastrar)  # Conecte o botão "Cadastrar" ao método

    def login(self):
        admin = "admin"
        senha = "admin"

        user = self.ui.email_input.text()  # Certifique-se de que o nome do campo de entrada está correto
        password = self.ui.senha_input.text()  # Certifique-se de que o nome do campo de entrada está correto

        if admin == user and password == senha:
            QMessageBox.information(self, "Login realizado!", "Login realizado com sucesso!")
            
        else:
            QMessageBox.warning(self, "Erro", "Erro no login ou senha")


app = QApplication(sys.argv)
window = login()
window.show()
sys.exit(app.exec_())