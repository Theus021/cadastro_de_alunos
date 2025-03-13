from operator import itemgetter
from tkinter.dialog import Dialog
from unittest import result
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QPushButton, QWidget, QDialog, QMessageBox
from PySide6.QtPrintSupport import *
from PySide6.QtWidgets import QTableWidgetItem
import sys
import os
from PySide6.QtCore import Qt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulos.cadastrarEntitade import Student_form, open_cadastrar_aluno
from modulos.atualizarEntidade import Entity_form
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

            aluno_id = row_data[0] 

            botoes = self.botoesDeAcao(aluno_id)
            self.ui.tableWidget_2.setCellWidget(row_index, 6, botoes)
            
        db.close_connection() 

    def botoesDeAcao(self, aluno_id ):
        
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.edit_button = QPushButton("✏️", self)
        self.edit_button.setStyleSheet("background-color: blue;")
        self.edit_button.setFixedSize(56, 26) 
        self.edit_button.clicked.connect(lambda: self.editarRegistros(aluno_id))

        self.delete_button = QPushButton("🗑️", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(56, 26)  
        self.delete_button.clicked.connect(lambda: self.deletarRegistro(aluno_id))   

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        return widget

    def editarRegistros(self, aluno_id): 
        db = Data_base()
        aluno = db.buscar_aluno_por_id(aluno_id)  # Busca os dados pelo ID
        db.close_connection()

        if aluno:
            dialog = Entity_form(aluno=aluno)  # Passa os dados para o formulário

            if dialog.exec_() == QDialog.Accepted:  # Se salvar os dados
                self.buscar_registros()  # Atualiza a tabela
        else:
            QMessageBox.warning(self, "Erro", "Aluno não encontrado no banco de dados.")

    def deletarRegistro(self, aluno_id):
        db = Data_base()
        db.connect()
        db.deletar_entidade(aluno_id)

        QMessageBox.information(self, "sucesso", "Registro excluido com sucesso !")
        self.buscar_registros()