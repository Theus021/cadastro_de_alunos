from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Data_base  
from telas.tela_request import Ui_Dialog

class RequestPassword(QDialog):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.cadastrar_button.clicked.connect(self.verifyPassword)  

        self.ui.senha_input.setEnabled(False)
        self.ui.senha_confirm_input.setEnabled(False)
        self.ui.email_input.textChanged.connect(self.verifyUser)

    def verifyUser(self):
        email = self.ui.email_input.text().strip()

        if not email:
            self.ui.senha_input.setEnabled(False)
            self.ui.senha_confirm_input.setEnabled(False)
            return

        db = Data_base()  
        db.connect()
        stored_email = db.confereEmail(email)

        if stored_email:
            self.ui.senha_input.setEnabled(True)
            self.ui.senha_confirm_input.setEnabled(True)
        else:
            self.ui.senha_input.setEnabled(False)
            self.ui.senha_confirm_input.setEnabled(False)

    def verifyPassword(self):

        senha = self.ui.senha_input.text().strip()
        confirm_senha = self.ui.senha_confirm_input.text().strip()
        email = self.ui.email_input.text().strip()

        if not senha or not confirm_senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos de senha!")
            return

        if len(senha) < 8:
             QMessageBox.warning(self, "Erro", "A senha deve ter pelo menos 8 caracteres!")

        if senha == confirm_senha:
            db = Data_base()
            db.connect()
            sucesso = db.alter_password(senha, email)

            if sucesso:
                QMessageBox.information(self, "Sucesso", "Senha atualizada com sucesso!")
                self.close()
        else:    
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

def request_password():
    request_window = RequestPassword()
    request_window.exec_()
