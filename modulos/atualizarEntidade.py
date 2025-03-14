from PySide6.QtWidgets import (QDialog, QMessageBox)
from PySide6.QtPrintSupport import *
import sys
import os
import re
from PySide6.QtCore import Qt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Data_base
from telas.register_student import Ui_Dialog

class Entity_form(QDialog):
    def __init__(self, aluno = None, *args, **argvs):
        super(Entity_form, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cadastrar_button.clicked.connect(self.salvar_alteracoes)
        self.ui.voltar_button.clicked.connect(self.close)
    
        self.aluno_cpf = None  

        if aluno:
            self.preencher_dados(aluno)
            self.aluno_cpf = aluno[2]

    def preencher_dados(self, aluno):
        
        self.ui.nome_input.setText(str(aluno[0]))  
        self.ui.email_imput.setText(str(aluno[1]))
        self.ui.cpf_input.setText(str(aluno[2])) 
        self.ui.nasc_input_2.setText(str(aluno[3])) 
        self.ui.nasc_input.setText(str(aluno[4]))  
        self.ui.estadoC_comboB.setCurrentText(str(aluno[5]))  
        self.ui.endereco_input.setText(str(aluno[6]))
        self.ui.sexo_ComboB.setCurrentText(str(aluno[7]))  
        self.ui.tel1_input_2.setText(str(aluno[8]))  
        self.ui.periodo_comboB.setCurrentText(str(aluno[9]))  
        self.ui.turma_comboB.setCurrentText(str(aluno[10]))  

        self.ui.cadastrar_button.setText("Salvar")
        self.ui.cpf_input.setEnabled(False)  
        self.ui.estadoC_comboB_2.setEnabled(False)  
    
    def salvar_alteracoes(self):
       
        nome = self.ui.nome_input.text()
        email = self.ui.email_imput.text()
        cpf = self.ui.cpf_input.text()  
        rg = self.ui.nasc_input_2.text()
        nasc = self.ui.nasc_input.text()
        estadoC = self.ui.estadoC_comboB.currentText()
        endereco = self.ui.endereco_input.text()
        sexo = self.ui.sexo_ComboB.currentText()
        tel = self.ui.tel1_input_2.text()
        periodo = self.ui.periodo_comboB.currentText()
        turma = self.ui.turma_comboB.currentText()
        ativo = 1

        if not all([nome, email, rg, cpf, endereco, sexo, nasc, tel, periodo, turma]):
            QMessageBox.information(self, "Campos vazios", "Preencha todos os campos")
            return

        db = Data_base()
        db.connect()
        
        fullDataSet = (nome, email, rg, estadoC, endereco, sexo, nasc, tel, periodo, turma, ativo, cpf)

        sucesso = db.atualizar_entidade(fullDataSet)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Dados atualizados com sucesso!")
            self.accept()  # Fecha o diálogo e retorna QDialog.Accepted
        else:
            QMessageBox.warning(self, "Erro", "Erro ao atualizar os dados do aluno.")

        db.close_connection()

def open_cadastrar_aluno():
    cadastro_de_estudante = Entity_form()
    cadastro_de_estudante.exec_()
