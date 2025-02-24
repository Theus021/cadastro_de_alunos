from PyQt5.QtWidgets import QDialog
from telas.register import Ui_Dialog

class cadastrar(QDialog):
    def __init__(self, *args, **argvs):
        super(cadastrar, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
def open_cadastrar():
    cadastro_window = cadastrar()
    cadastro_window.exec_()