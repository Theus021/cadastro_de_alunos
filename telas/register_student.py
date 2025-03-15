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
        self.nome_input.setGeometry(QRect(20, 50, 701, 40))
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
        self.email_text_input.setGeometry(QRect(20, 90, 141, 41))
        self.email_text_input.setFont(font)
        self.email_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.email_imput = QLineEdit(self.frame)
        self.email_imput.setObjectName(u"email_imput")
        self.email_imput.setGeometry(QRect(20, 130, 455, 40))
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
        self.cpf_text_input.setGeometry(QRect(20, 170, 141, 41))
        self.cpf_text_input.setFont(font)
        self.cpf_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.cpf_input = QLineEdit(self.frame)
        self.cpf_input.setObjectName(u"cpf_input")
        self.cpf_input.setGeometry(QRect(20, 210, 215, 40))
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
        self.estadoC_text_input.setGeometry(QRect(20, 250, 141, 41))
        self.estadoC_text_input.setFont(font)
        self.estadoC_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.estadoCivil_comboB = QComboBox(self.frame)
        self.estadoCivil_comboB.addItem("")
        self.estadoCivil_comboB.addItem("")
        self.estadoCivil_comboB.addItem("")
        self.estadoCivil_comboB.addItem("")
        self.estadoCivil_comboB.setObjectName(u"estadoC_comboB")
        self.estadoCivil_comboB.setGeometry(QRect(20, 290, 215, 40))
        self.estadoCivil_comboB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.estadoCivil_comboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
"image: url(:/principal/icon_seta_drop.png);\n"
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
        self.endereco_text_input.setGeometry(QRect(20, 330, 141, 41))
        self.endereco_text_input.setFont(font)
        self.endereco_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.endereco_input = QLineEdit(self.frame)
        self.endereco_input.setObjectName(u"endereco_input")
        self.endereco_input.setGeometry(QRect(20, 370, 371, 40))
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
        self.sexo_text_input.setGeometry(QRect(490, 90, 141, 41))
        self.sexo_text_input.setFont(font)
        self.sexo_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.sexo_ComboB = QComboBox(self.frame)
        self.sexo_ComboB.addItem("")
        self.sexo_ComboB.addItem("")
        self.sexo_ComboB.addItem("")
        self.sexo_ComboB.setObjectName(u"sexo_ComboB")
        self.sexo_ComboB.setGeometry(QRect(490, 130, 230, 40))
        self.sexo_ComboB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
"image: url(:/principal/icon_seta_drop.png);\n"
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
        self.nasc_text_input.setGeometry(QRect(490, 170, 141, 41))
        self.nasc_text_input.setFont(font)
        self.nasc_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.nascimento_input = QLineEdit(self.frame)
        self.nascimento_input.setObjectName(u"nasc_input")
        self.nascimento_input.setGeometry(QRect(490, 210, 230, 40))
        self.nascimento_input.setStyleSheet(u"QLineEdit{\n"
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
        self.rg_text_input.setGeometry(QRect(250, 170, 141, 41))
        self.rg_text_input.setFont(font)
        self.rg_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.rg_input = QLineEdit(self.frame)
        self.rg_input.setObjectName(u"nasc_input_2")
        self.rg_input.setGeometry(QRect(250, 210, 225, 40))
        self.rg_input.setStyleSheet(u"QLineEdit{\n"
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
        self.categoria_input = QLabel(self.frame)
        self.categoria_input.setObjectName(u"categoria_input")
        self.categoria_input.setGeometry(QRect(250, 250, 141, 41))
        self.categoria_input.setFont(font)
        self.categoria_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.cadastrar_button = QPushButton(self.frame)
        self.cadastrar_button.setObjectName(u"cadastrar_button")
        self.cadastrar_button.setGeometry(QRect(20, 430, 121, 41))
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
        self.voltar_button.setGeometry(QRect(160, 430, 94, 41))
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
        self.tel1_text_input_2.setGeometry(QRect(490, 250, 141, 41))
        self.tel1_text_input_2.setFont(font)
        self.tel1_text_input_2.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.telefone_input = QLineEdit(self.frame)
        self.telefone_input.setObjectName(u"tel1_input_2")
        self.telefone_input.setGeometry(QRect(490, 290, 230, 40))
        self.telefone_input.setStyleSheet(u"QLineEdit{\n"
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
        self.categoria_comboB = QComboBox(self.frame)
        self.categoria_comboB.addItem("")
        self.categoria_comboB.addItem("")
        self.categoria_comboB.addItem("")
        self.categoria_comboB.setObjectName(u"estadoC_comboB_2")
        self.categoria_comboB.setGeometry(QRect(250, 290, 225, 40))
        self.categoria_comboB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.categoria_comboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
"image: url(:/principal/icon_seta_drop.png);\n"
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
        self.periodoC_text_input = QLabel(self.frame)
        self.periodoC_text_input.setObjectName(u"periodoC_text_input")
        self.periodoC_text_input.setGeometry(QRect(410, 330, 141, 41))
        self.periodoC_text_input.setFont(font)
        self.periodoC_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.periodo_comboB = QComboBox(self.frame)
        self.periodo_comboB.addItem("")
        self.periodo_comboB.addItem("")
        self.periodo_comboB.addItem("")
        self.periodo_comboB.setObjectName(u"periodo_comboB")
        self.periodo_comboB.setGeometry(QRect(410, 370, 141, 40))
        self.periodo_comboB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.periodo_comboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
"image: url(:/principal/icon_seta_drop.png);\n"
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
        self.turma_text_input = QLabel(self.frame)
        self.turma_text_input.setObjectName(u"turma_text_input")
        self.turma_text_input.setGeometry(QRect(570, 330, 141, 41))
        self.turma_text_input.setFont(font)
        self.turma_text_input.setStyleSheet(u"QLabel{\n"
"color:#999A9A;\n"
" font-weight: 600;}")
        self.turma_comboB = QComboBox(self.frame)
        self.turma_comboB.addItem("")
        self.turma_comboB.addItem("")
        self.turma_comboB.addItem("")
        self.turma_comboB.addItem("")
        self.turma_comboB.addItem("")
        self.turma_comboB.setObjectName(u"turma_comboB")
        self.turma_comboB.setGeometry(QRect(570, 370, 151, 40))
        self.turma_comboB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.turma_comboB.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
"image: url(:/principal/icon_seta_drop.png);\n"
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
        self.turma_text_input.raise_()
        self.periodoC_text_input.raise_()
        self.endereco_text_input.raise_()
        self.tel1_text_input_2.raise_()
        self.categoria_input.raise_()
        self.estadoC_text_input.raise_()
        self.nasc_text_input.raise_()
        self.rg_text_input.raise_()
        self.cpf_text_input.raise_()
        self.sexo_text_input.raise_()
        self.email_text_input.raise_()
        self.nomeC_text_input.raise_()
        self.nome_input.raise_()
        self.email_imput.raise_()
        self.cpf_input.raise_()
        self.estadoCivil_comboB.raise_()
        self.endereco_input.raise_()
        self.sexo_ComboB.raise_()
        self.nascimento_input.raise_()
        self.rg_input.raise_()
        self.cadastrar_button.raise_()
        self.voltar_button.raise_()
        self.telefone_input.raise_()
        self.categoria_comboB.raise_()
        self.periodo_comboB.raise_()
        self.turma_comboB.raise_()
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1021, 51))
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
        self.cpf_input.setInputMask("")
        self.cpf_input.setText("")
        self.cpf_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o CPF", None))
        self.estadoC_text_input.setText(QCoreApplication.translate("Dialog", u"Estado civil", None))
        self.estadoCivil_comboB.setItemText(0, QCoreApplication.translate("Dialog", u"Estado civil", None))
        self.estadoCivil_comboB.setItemText(1, QCoreApplication.translate("Dialog", u"Solteiro", None))
        self.estadoCivil_comboB.setItemText(2, QCoreApplication.translate("Dialog", u"Casado", None))
        self.estadoCivil_comboB.setItemText(3, QCoreApplication.translate("Dialog", u"Vi\u00favo", None))

        self.endereco_text_input.setText(QCoreApplication.translate("Dialog", u"Endere\u00e7o  *", None))
        self.endereco_input.setText("")
        self.endereco_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o endere\u00e7o", None))
        self.sexo_text_input.setText(QCoreApplication.translate("Dialog", u"Sexo *", None))
        self.sexo_ComboB.setItemText(0, QCoreApplication.translate("Dialog", u"Sexo", None))
        self.sexo_ComboB.setItemText(1, QCoreApplication.translate("Dialog", u"Masculino", None))
        self.sexo_ComboB.setItemText(2, QCoreApplication.translate("Dialog", u"Feminino", None))

        self.nasc_text_input.setText(QCoreApplication.translate("Dialog", u"Nascimento *", None))
        self.nascimento_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite a data de nascimento", None))
        self.rg_text_input.setText(QCoreApplication.translate("Dialog", u"RG *", None))
        self.rg_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite o rg", None))
        self.categoria_input.setText(QCoreApplication.translate("Dialog", u"Categoria *", None))
        self.cadastrar_button.setText(QCoreApplication.translate("Dialog", u"Cadastrar", None))
        self.voltar_button.setText(QCoreApplication.translate("Dialog", u"Voltar", None))
        self.tel1_text_input_2.setText(QCoreApplication.translate("Dialog", u"Telefone 1 *", None))
        self.telefone_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite outro telefone", None))
        self.categoria_comboB.setItemText(0, QCoreApplication.translate("Dialog", u"Categoria", None))
        self.categoria_comboB.setItemText(1, QCoreApplication.translate("Dialog", u"Professor", None))
        self.categoria_comboB.setItemText(2, QCoreApplication.translate("Dialog", u"Aluno", None))

        self.periodoC_text_input.setText(QCoreApplication.translate("Dialog", u"Per\u00edodo", None))
        self.periodo_comboB.setItemText(0, QCoreApplication.translate("Dialog", u"Per\u00edodo", None))
        self.periodo_comboB.setItemText(1, QCoreApplication.translate("Dialog", u"Diurno", None))
        self.periodo_comboB.setItemText(2, QCoreApplication.translate("Dialog", u"Noturno", None))

        self.turma_text_input.setText(QCoreApplication.translate("Dialog", u"Turma", None))
        self.turma_comboB.setItemText(0, QCoreApplication.translate("Dialog", u"Turma", None))
        self.turma_comboB.setItemText(1, QCoreApplication.translate("Dialog", u"Ads", None))
        self.turma_comboB.setItemText(2, QCoreApplication.translate("Dialog", u"data-science", None))
        self.turma_comboB.setItemText(3, QCoreApplication.translate("Dialog", u"Machine-learning", None))
        self.turma_comboB.setItemText(4, QCoreApplication.translate("Dialog", u"Software-engineer", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u" Tech School", None))
    # retranslateUi

