import sys
import os
import re
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox)


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
        admin = False

        padrao_email = r"^[a-zA-Z0-9_.+-]+@(aluno\.faculdadeimpacta\.com\.br|colaborador\.faculdadeimpacta\.com\.br)$"
        
        if not user or not email or not confirmEmail or not password:
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return  # Sai da função para evitar continuar a execução

        if email != confirmEmail:
            QMessageBox.information(self, "Emails diferentes", "Os emails não coincidem")
            return

        if not re.match(padrao_email, email):  # Corrigido: usar 'email' e não 'emailAluno'
            QMessageBox.warning(self, "Erro", "Digite seu e-mail de aluno ou colaborador")
            return

        fullDataSet = (user, email, password, admin)
        db = Data_base()
        db.connect()
        db.create_table_new_user()

        dados = db.register_new_user(fullDataSet)

        if dados:
            QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
            self.ui.nome_input.clear()
            self.ui.email_input.clear()
            self.ui.email_input_2.clear()
            self.ui.senha_input.clear()
            self.close()
        else:
            QMessageBox.information(self, "Erro", "Aconteceu um erro inesperado")

        db.close_connection()    


def open_cadastrar():
    cadastro_window = Ui_dialog_login()
    cadastro_window.exec_()

   

    