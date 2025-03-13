import sys
import os
import re #regex
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox)
from db.database import Data_base


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telas.tela_register import Ui_Dialog
from db.database import Data_base

class Ui_dialog_login(QDialog):
    def __init__(self):
        super(Ui_dialog_login, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cadastrar_button.clicked.connect(self.cadastrar_usuarios)
        self.ui.close_button.clicked.connect(self.close)

    def cadastrar_usuarios(self):
        user = self.ui.nome_input.text().strip()
        email = self.ui.email_input.text().strip()
        confirmEmail = self.ui.email_input_2.text().strip()
        password = self.ui.senha_input.text().strip()
        admin = 0

        padrao_email = r"^[a-zA-Z0-9_.+-]+@(colaborador\.impacta\.com\.br)$"


        db = Data_base()
        db.connect()
        verificaEmail = db.confereEmail(email)

        if verificaEmail:
            QMessageBox.information(self, "Error", "Email Já cadastrado !")
   
        
        if not user or not email or not confirmEmail or not password:
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return  # Sai da função para evitar continuar a execução

        if email != confirmEmail:
            QMessageBox.information(self, "Emails diferentes", "Os emails não coincidem")
            return

        if not re.match(padrao_email, email): 
            QMessageBox.warning(self, "Erro", "Digite seu e-mail de colaborador")
            return

        if len(password) < 8:
            QMessageBox.warning(self, "Erro", "A senha deve ter pelo menos 8 caracteres!")
            return

        fullDataSet = (user, email, password, admin)
        db = Data_base()
        db.connect()
        db.create_table_new_user()

        dados = db.register_new_user(fullDataSet)

        if dados:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso !")
            self.ui.nome_input.clear()
            self.ui.email_input.clear()
            self.ui.email_input_2.clear()
            self.ui.senha_input.clear()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Email já cadastrado !")

        db.close_connection()    


def open_cadastrar():
    cadastro_window = Ui_dialog_login()
    cadastro_window.exec_()


   

    