from operator import itemgetter
from unittest import result
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtPrintSupport import *
from PySide6.QtWidgets import QTableWidgetItem
import sys
import os
from PySide6.QtCore import Qt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulos.registerSchool import open_cadastrar_aluno
from telas.tela_home import Ui_MainWindow
from db.database import Data_base

class telaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.adicionar_button.clicked.connect(open_cadastrar_aluno)
        self.buscar_registros()

    def buscar_registros(self):
        db = Data_base()
        resultado = db.select_all_users()
        
        self.ui.tableWidget_2.setColumnWidth(0, 50)
        self.ui.tableWidget_2.setColumnWidth(1, 200)
        self.ui.tableWidget_2.setColumnWidth(2, 150)
        self.ui.tableWidget_2.setColumnWidth(3, 150)
        self.ui.tableWidget_2.setColumnWidth(4, 80)
        self.ui.tableWidget_2.setColumnWidth(5, 120)
        self.ui.tableWidget_2.setColumnWidth(6, 125)
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(len(resultado))

        for row_index, row_data in enumerate(resultado):
            for col_index, cell_data  in enumerate(row_data):
                
                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignCenter)
        
                self.ui.tableWidget_2.setItem(row_index, col_index, item)

        db.close_connection()        

    def atualizarRegistros(self):
        db = Data_base()
        db.select_all_users()