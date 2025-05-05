from PySide6.QtWidgets import (QDialog, QMessageBox)
from PySide6.QtPrintSupport import *
from datetime import datetime
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Data_base
from telas.register_student import Ui_Dialog
from PySide6.QtCore import QEvent, Qt

class Student_form(QDialog):
    def __init__(self, atualizar_callback=None, *args, **argvs):
        super(Student_form, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cadastrar_button.clicked.connect(self.cadastrar_entidade)
        self.ui.voltar_button.clicked.connect(self.close)

        self.ui.nascimento_input.installEventFilter(self)
        self.ui.cpf_input.installEventFilter(self)
        self.ui.rg_input.installEventFilter(self)
        self.ui.telefone_input.installEventFilter(self)

        self.atualizar_callback = atualizar_callback


    def ativar_mascara_data(self):
        self.ui.nascimento_input.setInputMask("00/00/0000;_")

    def ativar_mascara_cpf(self):
        self.ui.cpf_input.setInputMask("000.000.000-00;_")

    def ativar_mascara_rg(self):
        self.ui.rg_input.setInputMask("00.000.000-0;_")

    def ativar_mascara_telefone(self):
        self.ui.telefone_input.setInputMask("(00) 00000-0000;_")    

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            if obj == self.ui.nascimento_input:
                self.ui.nascimento_input.setInputMask("00/00/0000;_")
            elif obj == self.ui.cpf_input:
                self.ui.cpf_input.setInputMask("000.000.000-00;_")
            elif obj == self.ui.rg_input:
                self.ui.rg_input.setInputMask("00.000.000-0;_")
            elif obj == self.ui.telefone_input:
                self.ui.telefone_input.setInputMask("(00) 00000-0000;_")    
        return super().eventFilter(obj, event)

    def cadastrar_entidade(self):
        nome = self.ui.nome_input.text()
        email = self.ui.email_imput.text()
        cpf = self.ui.cpf_input.text()
        rg = self.ui.rg_input.text()
        nascimento = self.ui.nascimento_input.text()
        estadoC = self.ui.estadoCivil_comboB.currentText()
        endereco = self.ui.endereco_input.text()
        sexo = self.ui.sexo_ComboB.currentText()
        nasc_formatada = self.ui.nascimento_input.text()
        tel= self.ui.telefone_input.text()
        periodo = self.ui.periodo_comboB.currentText()
        turma = self.ui.turma_comboB.currentText()
        categoria = self.ui.categoria_comboB.currentText()
        ativo = 1

        if not all([nome, email, cpf, rg, endereco, sexo, nascimento, tel, categoria, periodo, turma]):
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return
        
        try:
            nasc_formatada = datetime.strptime(nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            QMessageBox.warning(self, "Erro", "Data de nascimento inválida. Use o formato DD/MM/AAAA.")
            return

        fullDataSet = (nome, email, cpf, rg, estadoC, endereco, sexo, nasc_formatada, tel, categoria, periodo, turma, ativo)
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