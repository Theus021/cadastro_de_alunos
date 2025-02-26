from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos.login import login

app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = login()
    window.show()
    sys.exit(app.exec_())
