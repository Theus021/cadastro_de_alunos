import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox)
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
            db = Data_base()
            db.connect()

            user = self.ui.nome_input.text()
            email = self.ui.email_input.text()
            confirmEmail = self.ui.email_input_2.text()
            password = self.ui.senha_input.text()
            admin = False
        
            if user == "" or email == "" or confirmEmail == "" or password == "":
                QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            elif email != confirmEmail:
                QMessageBox.information(self, "Emails diferentes", "Os emails não coincidem")
            else:
                fullDataSet = (user, email, password, admin)
                db = Data_base()
                db.connect()
                db.create_table_new_user()
                db.register_new_user(fullDataSet)
                QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
                self.ui.nome_input.clear()
                self.ui.email_input.clear()
                self.ui.email_input_2.clear()
                self.ui.senha_input.clear()
                self.close()

def open_cadastrar():
    db = Data_base()
    db.connect()
    db.create_table_new_user()
    db.close_connection()
    
    cadastro_window = Ui_dialog_login()
    cadastro_window.exec_()

   

    