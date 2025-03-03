# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_student.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import telas.toolBar_rc
import telas.principal_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 80, 741, 491))
        self.frame.setStyleSheet(u"QFrame{\n"
"background:#FFF;\n"
"border-radius:15px;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nomeC_text_input = QLabel(self.frame)
        self.nomeC_text_input.setObjectName(u"nomeC_text_input")
        self.nomeC_text_input.setGeometry(QRect(20, 10, 141, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.nomeC_text_input.setFont(font)
        self.nomeC_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.nome_input = QLineEdit(self.frame)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setGeometry(QRect(20, 50, 701, 41))
        self.nome_input.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.email_text_input = QLabel(self.frame)
        self.email_text_input.setObjectName(u"email_text_input")
        self.email_text_input.setGeometry(QRect(20, 100, 141, 41))
        self.email_text_input.setFont(font)
        self.email_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.email_imput = QLineEdit(self.frame)
        self.email_imput.setObjectName(u"email_imput")
        self.email_imput.setGeometry(QRect(20, 140, 455, 41))
        self.email_imput.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.cpf_text_input = QLabel(self.frame)
        self.cpf_text_input.setObjectName(u"cpf_text_input")
        self.cpf_text_input.setGeometry(QRect(20, 190, 141, 41))
        self.cpf_text_input.setFont(font)
        self.cpf_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.cpf_input = QLineEdit(self.frame)
        self.cpf_input.setObjectName(u"cpf_input")
        self.cpf_input.setGeometry(QRect(20, 230, 215, 41))
        self.cpf_input.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.estadoC_text_input = QLabel(self.frame)
        self.estadoC_text_input.setObjectName(u"estadoC_text_input")
        self.estadoC_text_input.setGeometry(QRect(20, 280, 141, 41))
        self.estadoC_text_input.setFont(font)
        self.estadoC_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.estadoC_comboB = QComboBox(self.frame)
        self.estadoC_comboB.addItem("")
        self.estadoC_comboB.addItem("")
        self.estadoC_comboB.addItem("")
        self.estadoC_comboB.setObjectName(u"estadoC_comboB")
        self.estadoC_comboB.setGeometry(QRect(20, 320, 215, 41))
        self.estadoC_comboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:10px;\n"
"background: #fff;\n"
"transition: border 0.2s ease-in-out;\n"
"color: #727474;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border: 0px\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"image: url(:/principal/icons8-seta-para-expandir-15.png);\n"
"width: 12px;\n"
"height:12px;\n"
"margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"border: 2px solid #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"font-size: 12px;\n"
"background-color: #fff;\n"
"outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView::item {\n"
"padding-left: 10px;\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
" background-color: #1e90ff;\n"
" }\n"
"\n"
"QComboBox QListView::item:selected {\n"
"background-color: #1e90ff;\n"
" }")
        self.endereco_text_input = QLabel(self.frame)
        self.endereco_text_input.setObjectName(u"endereco_text_input")
        self.endereco_text_input.setGeometry(QRect(20, 370, 141, 41))
        self.endereco_text_input.setFont(font)
        self.endereco_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.endereco_input = QLineEdit(self.frame)
        self.endereco_input.setObjectName(u"endereco_input")
        self.endereco_input.setGeometry(QRect(20, 410, 455, 41))
        self.endereco_input.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.sexo_text_input = QLabel(self.frame)
        self.sexo_text_input.setObjectName(u"sexo_text_input")
        self.sexo_text_input.setGeometry(QRect(490, 100, 141, 41))
        self.sexo_text_input.setFont(font)
        self.sexo_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.sexo_ComboB = QComboBox(self.frame)
        self.sexo_ComboB.addItem("")
        self.sexo_ComboB.addItem("")
        self.sexo_ComboB.setObjectName(u"sexo_ComboB")
        self.sexo_ComboB.setGeometry(QRect(490, 140, 230, 41))
        self.sexo_ComboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:10px;\n"
"background: #fff;\n"
"transition: border 0.2s ease-in-out;\n"
"color: #727474;\n"
"font-size: 14px\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border: 0px\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"image: url(:/principal/icons8-seta-para-expandir-15.png);\n"
"width: 12px;\n"
"height:12px;\n"
"margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"border: 2px solid #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"font-size: 12px;\n"
"background-color: #fff;\n"
"outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView::item {\n"
"padding-left: 10px;\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
" background-color: #1e90ff;\n"
" }\n"
"\n"
"QComboBox QListView::item:selected {\n"
"background-color: #1e90ff;\n"
" }")
        self.nasc_text_input = QLabel(self.frame)
        self.nasc_text_input.setObjectName(u"nasc_text_input")
        self.nasc_text_input.setGeometry(QRect(490, 190, 141, 41))
        self.nasc_text_input.setFont(font)
        self.nasc_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.nasc_input = QLineEdit(self.frame)
        self.nasc_input.setObjectName(u"nasc_input")
        self.nasc_input.setGeometry(QRect(490, 230, 230, 41))
        self.nasc_input.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.rg_text_input = QLabel(self.frame)
        self.rg_text_input.setObjectName(u"rg_text_input")
        self.rg_text_input.setGeometry(QRect(250, 190, 141, 41))
        self.rg_text_input.setFont(font)
        self.rg_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.nasc_input_2 = QLineEdit(self.frame)
        self.nasc_input_2.setObjectName(u"nasc_input_2")
        self.nasc_input_2.setGeometry(QRect(250, 230, 225, 41))
        self.nasc_input_2.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.tel_text_input = QLabel(self.frame)
        self.tel_text_input.setObjectName(u"tel_text_input")
        self.tel_text_input.setGeometry(QRect(490, 280, 141, 41))
        self.tel_text_input.setFont(font)
        self.tel_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.tel2_input = QLineEdit(self.frame)
        self.tel2_input.setObjectName(u"tel2_input")
        self.tel2_input.setGeometry(QRect(490, 320, 230, 41))
        self.tel2_input.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.cadastrar_button = QPushButton(self.frame)
        self.cadastrar_button.setObjectName(u"cadastrar_button")
        self.cadastrar_button.setGeometry(QRect(599, 410, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.cadastrar_button.setFont(font1)
        self.cadastrar_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cadastrar_button.setStyleSheet(u"QPushButton{\n"
"background: #32CD32;\n"
"color: #FFF;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #39DD39;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"border: 3px solid #CCC\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/principal/icons8-soma-20.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cadastrar_button.setIcon(icon)
        self.cadastrar_button.setIconSize(QSize(25, 30))
        self.voltar_button = QPushButton(self.frame)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(490, 410, 94, 41))
        font2 = QFont()
        font2.setBold(True)
        self.voltar_button.setFont(font2)
        self.voltar_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.voltar_button.setStyleSheet(u"QPushButton{\n"
" background-color: #f72585;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"	border-radius: 4px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/cadastro/icons8-esquerda-30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.voltar_button.setIcon(icon1)
        self.voltar_button.setIconSize(QSize(25, 30))
        self.tel1_text_input_2 = QLabel(self.frame)
        self.tel1_text_input_2.setObjectName(u"tel1_text_input_2")
        self.tel1_text_input_2.setGeometry(QRect(250, 280, 141, 41))
        self.tel1_text_input_2.setFont(font)
        self.tel1_text_input_2.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.tel1_input_2 = QLineEdit(self.frame)
        self.tel1_input_2.setObjectName(u"tel1_input_2")
        self.tel1_input_2.setGeometry(QRect(250, 320, 225, 41))
        self.tel1_input_2.setStyleSheet(u"QLineEdit{\n"
"font-size:14px;\n"
"background: #FFFFFF;\n"
"border: 1px solid #ccc;\n"
"padding-left:15px;\n"
"border-radius: 4px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.email_text_input.raise_()
        self.nomeC_text_input.raise_()
        self.nome_input.raise_()
        self.email_imput.raise_()
        self.cpf_text_input.raise_()
        self.cpf_input.raise_()
        self.estadoC_text_input.raise_()
        self.estadoC_comboB.raise_()
        self.endereco_text_input.raise_()
        self.endereco_input.raise_()
        self.sexo_text_input.raise_()
        self.sexo_ComboB.raise_()
        self.nasc_text_input.raise_()
        self.nasc_input.raise_()
        self.rg_text_input.raise_()
        self.nasc_input_2.raise_()
        self.tel_text_input.raise_()
        self.tel2_input.raise_()
        self.cadastrar_button.raise_()
        self.voltar_button.raise_()
        self.tel1_text_input_2.raise_()
        self.tel1_input_2.raise_()
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 51))
        self.widget.setStyleSheet(u"QWidget{\n"
"background:#0265CB\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"color: #FFF;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.nomeC_text_input.setText(QCoreApplication.translate("Dialog", u"Nome completo *", None))
        self.nome_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o nome completo", None))
        self.email_text_input.setText(QCoreApplication.translate("Dialog", u"E-mail *", None))
        self.email_imput.setText("")
        self.email_imput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o e-mail", None))
        self.cpf_text_input.setText(QCoreApplication.translate("Dialog", u"CPF *", None))
        self.cpf_input.setText("")
        self.cpf_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o CPF", None))
        self.estadoC_text_input.setText(QCoreApplication.translate("Dialog", u"Estado civil", None))
        self.estadoC_comboB.setItemText(0, QCoreApplication.translate("Dialog", u"Solteiro", None))
        self.estadoC_comboB.setItemText(1, QCoreApplication.translate("Dialog", u"Casado", None))
        self.estadoC_comboB.setItemText(2, QCoreApplication.translate("Dialog", u"Vi\u00favo", None))

        self.endereco_text_input.setText(QCoreApplication.translate("Dialog", u"Endere\u00e7o  *", None))
        self.endereco_input.setText("")
        self.endereco_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o endere\u00e7o", None))
        self.sexo_text_input.setText(QCoreApplication.translate("Dialog", u"Sexo *", None))
        self.sexo_ComboB.setItemText(0, QCoreApplication.translate("Dialog", u"Masculino", None))
        self.sexo_ComboB.setItemText(1, QCoreApplication.translate("Dialog", u"Femino", None))

        self.nasc_text_input.setText(QCoreApplication.translate("Dialog", u"Nascimento *", None))
        self.nasc_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite a data de nascimento", None))
        self.rg_text_input.setText(QCoreApplication.translate("Dialog", u"RG *", None))
        self.nasc_input_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o rg", None))
        self.tel_text_input.setText(QCoreApplication.translate("Dialog", u"Telefone 2*", None))
        self.tel2_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite outro telefone", None))
        self.cadastrar_button.setText(QCoreApplication.translate("Dialog", u"Cadastrar", None))
        self.voltar_button.setText(QCoreApplication.translate("Dialog", u"Voltar", None))
        self.tel1_text_input_2.setText(QCoreApplication.translate("Dialog", u"Telefone 1 *", None))
        self.tel1_input_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite outro telefone", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"  Cadastro de Aluno", None))
    # retranslateUi

