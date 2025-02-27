# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
import telas.login_rc

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        if not Dialog_login.objectName():
            Dialog_login.setObjectName(u"Dialog_login")
        Dialog_login.resize(800, 597)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_login.sizePolicy().hasHeightForWidth())
        Dialog_login.setSizePolicy(sizePolicy)
        Dialog_login.setStyleSheet(u"QDialog{\n"
"background: #FFF;\n"
"}")
        self.frame = QFrame(Dialog_login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 59, 370, 481))
        self.frame.setMinimumSize(QSize(370, 481))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"QFrame{\n"
"background: #FFFFFF;\n"
"border-radius:7px;\n"
"box-shadow: 10px 10px 40px rgba(0, 0, 0, 0.4);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.fixed_text = QTextEdit(self.frame)
        self.fixed_text.setObjectName(u"fixed_text")
        self.fixed_text.setGeometry(QRect(30, 80, 281, 51))
        self.fixed_text.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.fixed_text.setStyleSheet(u"QTextEdit{\n"
"background:#FFF\n"
"}")
        self.fixed_text.setReadOnly(True)
        self.fixed_text.setTextInteractionFlags(Qt.NoTextInteraction)
        self.login_text = QTextEdit(self.frame)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setGeometry(QRect(30, 30, 121, 51))
        self.login_text.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.login_text.setReadOnly(True)
        self.email_text_input = QTextEdit(self.frame)
        self.email_text_input.setObjectName(u"email_text_input")
        self.email_text_input.setGeometry(QRect(30, 130, 111, 31))
        self.email_text_input.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.email_text_input.setReadOnly(True)
        self.email_input = QLineEdit(self.frame)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(30, 160, 311, 41))
        self.email_input.setStyleSheet(u"QLineEdit{\n"
"border-radius: 4px;\n"
"border: 1px solid #ccc;\n"
"padding-left:10px;\n"
"font-size:14px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.senha_text_input = QTextEdit(self.frame)
        self.senha_text_input.setObjectName(u"senha_text_input")
        self.senha_text_input.setGeometry(QRect(30, 220, 111, 31))
        self.senha_text_input.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.senha_text_input.setReadOnly(True)
        self.senha_input = QLineEdit(self.frame)
        self.senha_input.setObjectName(u"senha_input")
        self.senha_input.setGeometry(QRect(30, 250, 311, 41))
        self.senha_input.setStyleSheet(u"QLineEdit{\n"
"border-radius: 4px;\n"
"border: 1px solid #ccc;\n"
"padding-left:10px;\n"
"font-size:14px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.entrar_button = QPushButton(self.frame)
        self.entrar_button.setObjectName(u"entrar_button")
        self.entrar_button.setGeometry(QRect(30, 360, 311, 41))
        self.entrar_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.entrar_button.setStyleSheet(u"QPushButton{\n"
" background-color: #2079D5;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"	border-radius: 4px;\n"
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
        self.cadastrar_button = QPushButton(self.frame)
        self.cadastrar_button.setObjectName(u"cadastrar_button")
        self.cadastrar_button.setGeometry(QRect(30, 420, 311, 41))
        self.cadastrar_button.setMinimumSize(QSize(0, 41))
        self.cadastrar_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cadastrar_button.setStyleSheet(u"QPushButton{\n"
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
        self.email_person_icon = QLabel(self.frame)
        self.email_person_icon.setObjectName(u"email_person_icon")
        self.email_person_icon.setGeometry(QRect(310, 170, 20, 20))
        self.email_person_icon.setStyleSheet(u"QLabel{\n"
"background:url(:/login/icons8-pessoa-do-sexo-masculino-100-1.png)\n"
"}\n"
"")
        self.email_div = QFrame(self.frame)
        self.email_div.setObjectName(u"email_div")
        self.email_div.setGeometry(QRect(300, 170, 1, 20))
        self.email_div.setStyleSheet(u"Line{\n"
"background: #ccc}")
        self.email_div.setFrameShape(QFrame.Shape.VLine)
        self.email_div.setFrameShadow(QFrame.Shadow.Sunken)
        self.senha_div = QFrame(self.frame)
        self.senha_div.setObjectName(u"senha_div")
        self.senha_div.setGeometry(QRect(300, 260, 1, 20))
        self.senha_div.setStyleSheet(u"Line{\n"
"background: #ccc}")
        self.senha_div.setFrameShape(QFrame.Shape.VLine)
        self.senha_div.setFrameShadow(QFrame.Shadow.Sunken)
        self.senha_icon = QLabel(self.frame)
        self.senha_icon.setObjectName(u"senha_icon")
        self.senha_icon.setGeometry(QRect(310, 260, 20, 20))
        self.senha_icon.setStyleSheet(u"QLabel{\n"
"background:url(:/login/icons8-cadeado-100.png)\n"
"}\n"
"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(24, 300, 151, 31))
        font = QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background:#fff;\n"
"color: #989999;\n"
"border:none;\n"
"padding-left: 0px\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"color:#757575\n"
"}")
        self.email_text_input.raise_()
        self.fixed_text.raise_()
        self.login_text.raise_()
        self.senha_text_input.raise_()
        self.senha_input.raise_()
        self.entrar_button.raise_()
        self.cadastrar_button.raise_()
        self.email_input.raise_()
        self.email_person_icon.raise_()
        self.email_div.raise_()
        self.senha_div.raise_()
        self.senha_icon.raise_()
        self.pushButton.raise_()
        self.background_blue = QWidget(Dialog_login)
        self.background_blue.setObjectName(u"background_blue")
        self.background_blue.setGeometry(QRect(0, 0, 800, 600))
        self.background_blue.setStyleSheet(u"QWidget{\n"
"background:#0265CB; \n"
"}")
        self.background_blue.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog_login)

        QMetaObject.connectSlotsByName(Dialog_login)
    # setupUi

    def retranslateUi(self, Dialog_login):
        Dialog_login.setWindowTitle(QCoreApplication.translate("Dialog_login", u"Dialog", None))
        self.fixed_text.setHtml(QCoreApplication.translate("Dialog_login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#666666;\">Digite os seus dados nos campos abaixo.</span></p></body></html>", None))
        self.login_text.setHtml(QCoreApplication.translate("Dialog_login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696; color:#284658;\">Login</span></p></body></html>", None))
        self.email_text_input.setHtml(QCoreApplication.translate("Dialog_login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696; color:#2d4a5c;\">E-mail</span></p></body></html>", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("Dialog_login", u"Digite seu e-mail", None))
        self.senha_text_input.setHtml(QCoreApplication.translate("Dialog_login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696; color:#2d4a5c;\">Senha</span></p></body></html>", None))
        self.senha_input.setPlaceholderText(QCoreApplication.translate("Dialog_login", u"Digite sua senha", None))
        self.entrar_button.setText(QCoreApplication.translate("Dialog_login", u"ENTRAR", None))
        self.cadastrar_button.setText(QCoreApplication.translate("Dialog_login", u"CADASTRAR", None))
        self.email_person_icon.setText("")
        self.senha_icon.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog_login", u"Esqueci minha senha", None))
    # retranslateUi

