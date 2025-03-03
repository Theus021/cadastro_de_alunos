from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telas.tela_login import Ui_Dialog_login
from modulos.registerM import open_cadastrar
from modulos.pagina_inicial import telaPrincipal
from db.database import Data_base

class Login(QDialog):  # Nome da classe começa com maiúscula por convenção
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_login()
        self.ui.setupUi(self)
        
        self.ui.entrar_button.clicked.connect(self.login)
        self.ui.cadastrar_button.clicked.connect(open_cadastrar)

    def login(self):
        user = self.ui.email_input.text().strip()
        password = self.ui.senha_input.text().strip()

        if not user or not password:
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return

        db = Data_base()
        db.connect()
        dados = db.pega_dados("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (user, password))

        if dados:
            QMessageBox.information(self, "Login realizado!", "Login realizado com sucesso!")
            self.close()  # Fecha a tela de login
            self.window = telaPrincipal()  # Certifique-se de que telaPrincipal herda de QMainWindow
            self.window.show()
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha inválidos")

        db.close_connection()

# Criando a aplicação e executando
app = QApplication(sys.argv)
window = Login()  # Aqui usamos a classe corrigida
window.show()
sys.exit(app.exec_())
