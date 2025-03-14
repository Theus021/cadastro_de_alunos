from PySide6.QtWidgets import (QDialog, QMessageBox)
from PySide6.QtPrintSupport import *
import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Data_base
from telas.register_student import Ui_Dialog

class Student_form(QDialog):
    def __init__(self, atualizar_callback=None, *args, **argvs):
        super(Student_form, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cadastrar_button.clicked.connect(self.cadastrar_entidade)
        self.ui.voltar_button.clicked.connect(self.close)

        self.atualizar_callback = atualizar_callback

    def cadastrar_entidade(self):
        nome = self.ui.nome_input.text()
        email = self.ui.email_imput.text()
        cpf = self.ui.cpf_input.text()
        rg = self.ui.nasc_input_2.text()
        nascimento = self.ui.nasc_input.text()
        estadoC = self.ui.estadoC_comboB.currentText()
        endereco = self.ui.endereco_input.text()
        sexo = self.ui.sexo_ComboB.currentText()
        nasc = self.ui.nasc_input.text()
        tel= self.ui.tel1_input_2.text()
        periodo = self.ui.periodo_comboB.currentText()
        turma = self.ui.turma_comboB.currentText()
       

        categoria = self.ui.estadoC_comboB_2.currentText()

        if not all([nome, email, cpf, rg, endereco, sexo, nascimento, tel, categoria, periodo, turma]):
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return

        ativo = 1
        
        fullDataSet = (nome, email, cpf, rg, estadoC, endereco, sexo, nasc, tel, categoria, periodo, turma, ativo)
        db = Data_base()
        db.connect()

        db.create_table_new_entidade()

        verificaEmail = db.verificaEmail(email)
        if verificaEmail:
            QMessageBox.warning(self, "Erro", "Email já cadastrado !")
                 
        sucesso = db.register_new_entidade(fullDataSet)

        if sucesso == "duplicate_entry":
            QMessageBox.warning(self, "Erro", "Email ou CPF já cadastrado !")

        elif sucesso:
            QMessageBox.information(self, "Sucesso", f"{categoria} cadastrado com sucesso !")
            if self.atualizar_callback:
                self.atualizar_callback()

            self.close()    

        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar usuário no sistema.")    
        
        db.close_connection()

def open_cadastrar_aluno():
    cadastro_de_estudante = Student_form()
    cadastro_de_estudante.exec_()
