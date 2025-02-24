from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtPrintSupport import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telas.pagina_inicial import Ui_home

class telaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_home()
        self.ui.setupUi(self)
        