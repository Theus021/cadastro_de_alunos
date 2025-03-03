from PySide6.QtWidgets import (QDialog, QMessageBox)
from PySide6.QtPrintSupport import *
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Data_base
from telas.register_student import Ui_Dialog

class Student_form(QDialog):
    def __init__(self, *args, **argvs):
        super(Student_form, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cadastrar_button.clicked.connect(self.cadastrar_aluno)
        self.ui.voltar_button.clicked.connect(self.close)
        
    def cadastrar_aluno(self):
        nomeAluno = self.ui.nome_input.text()
        emailAluno = self.ui.email_imput.text()
        cpfAluno = self.ui.cpf_input.text()
        rgAluno = self.ui.nasc_input_2.text()
        estadoCAluno = self.ui.estadoC_comboB.currentText()
        enderecoAluno = self.ui.endereco_input.text()
        sexoAluno = self.ui.sexo_ComboB.currentText()
        nasc = self.ui.nasc_input.text()
        tel1= self.ui.tel1_input_2.text()
        tel2 = self.ui.tel2_input.text()

        if nomeAluno == "" or emailAluno == "" or cpfAluno == "" or rgAluno == "" or estadoCAluno == "" or enderecoAluno == "" or sexoAluno == "" or nasc == "" or tel1 == "" or tel2 == "":
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")

        else:
            fullDataSet = (nomeAluno, emailAluno, cpfAluno, rgAluno, estadoCAluno, enderecoAluno, sexoAluno, nasc, tel1, tel2)
            db = Data_base()
            db.connect()
            db.create_table_new_student()

            dados = db.register_new_student(fullDataSet)  
            
            if dados:
                QMessageBox.information(self, 'Sucesso', 'Usuário cadastrado com sucesso !')
                self.close()
                db.close_connection()

            else:
                QMessageBox.information(self, 'Erro', 'Erro ao cadastrar dados no sistema')     

def open_cadastrar_aluno():
    cadastro_de_estudante = Student_form()
    cadastro_de_estudante.exec_()
