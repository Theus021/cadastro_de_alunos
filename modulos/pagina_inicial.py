from unittest import result
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtPrintSupport import *
from PySide6.QtWidgets import QTableWidgetItem
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulos.registerStudant import open_cadastrar_aluno
from telas.tela_home import Ui_MainWindow
from db.database import Data_base

class telaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.adicionar_aluno_button.clicked.connect(open_cadastrar_aluno)

