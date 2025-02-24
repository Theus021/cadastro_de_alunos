from PyQt5.QtWidgets import QDialog, QMessageBox
from telas.register import Ui_Dialog

class cadastrar(QDialog):
    def __init__(self, *args, **argvs):
        super(cadastrar, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.cadastrar_button.clicked.connect(self.cadastrar)    

    def cadastrar(self):
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
            QMessageBox.information(self, "Cadastro realizado!", "Cadastro realizado com sucesso!")
            self.close()


def open_cadastrar():
    cadastro_window = cadastrar()
    cadastro_window.exec_()