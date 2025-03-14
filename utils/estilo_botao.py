from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtPrintSupport import *
import sys
import os
from PySide6.QtCore import Qt, QSize

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulos.atualizarEntidade import Entity_form
from telas.tela_home import Ui_MainWindow
from db.database import Data_base


def botoesDeAcao(self, aluno_id ):
        
    widget = QWidget()
    layout = QHBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)

    self.edit_button = QPushButton("", self)
    icon1 = QIcon()
    icon1.addFile(u":/principal/icon_lápis_30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    self.edit_button.setIcon(icon1)
    self.edit_button.setIconSize(QSize(15, 15))
    self.edit_button.setStyleSheet(u"QPushButton{\n"
"    background-color: #2079D5;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"	 border-radius: 1px;\n"
"    font-weight: bold;\n"
"    cursor: pointer;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #2682E1;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"border: 3px solid #CCC\n"
"}")
    self.edit_button.setFixedSize(56, 26) 
    self.edit_button.clicked.connect(lambda: self.editarRegistros(aluno_id))

    self.delete_button = QPushButton("", self)
    icon2 = QIcon()
    icon2.addFile(u":/principal/icon_lixeira_30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    self.delete_button.setIcon(icon2)
    self.delete_button.setIconSize(QSize(22, 22))
    self.delete_button.setStyleSheet(u"QPushButton{\n"
"    background-color: #f72585;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"	 border-radius: 1px;\n"
"    font-weight: bold;\n"
"    cursor: pointer;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #FF3591; }\n"
"\n"
"QPushButton:clicked{\n"
"border: 3px solid #CCC\n"
"}")
    self.delete_button.setFixedSize(56, 26)  
    self.delete_button.clicked.connect(lambda: self.deletarRegistro(aluno_id))   

    layout.addWidget(self.edit_button)
    layout.addWidget(self.delete_button)
    return widget

