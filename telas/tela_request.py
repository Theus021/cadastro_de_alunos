# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_request.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(810, 600)
        Dialog.setStyleSheet(u"QDialog{\n"
"background: #FFF;\n"
"}\n"
"")
        self.frame = QFrame(Dialog)
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
        self.login_text = QTextEdit(self.frame)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setGeometry(QRect(30, 20, 201, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.login_text.setFont(font)
        self.login_text.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.login_text.setReadOnly(True)
        self.email_text_input = QTextEdit(self.frame)
        self.email_text_input.setObjectName(u"email_text_input")
        self.email_text_input.setGeometry(QRect(30, 140, 91, 31))
        self.email_text_input.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.email_text_input.setReadOnly(True)
        self.email_input = QLineEdit(self.frame)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(30, 170, 311, 41))
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
        self.email_div_input = QFrame(self.frame)
        self.email_div_input.setObjectName(u"email_div_input")
        self.email_div_input.setGeometry(QRect(300, 180, 2, 20))
        self.email_div_input.setStyleSheet(u"Line{\n"
"background: #ccc}")
        self.email_div_input.setFrameShape(QFrame.Shape.VLine)
        self.email_div_input.setFrameShadow(QFrame.Shadow.Sunken)
        self.email_icon = QLabel(self.frame)
        self.email_icon.setObjectName(u"email_icon")
        self.email_icon.setGeometry(QRect(310, 180, 20, 20))
        self.email_icon.setStyleSheet(u"QLabel{\n"
"background:url(:/login/icons8-mensagem-20.png)\n"
"}\n"
"")
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
        self.email_icon_2 = QLabel(self.frame)
        self.email_icon_2.setObjectName(u"email_icon_2")
        self.email_icon_2.setGeometry(QRect(310, 260, 20, 20))
        self.email_icon_2.setStyleSheet(u"QLabel{\n"
"background:url(:/login/icons8-cadeado-100.png);\n"
"}\n"
"")
        self.email_text_input_2 = QTextEdit(self.frame)
        self.email_text_input_2.setObjectName(u"email_text_input_2")
        self.email_text_input_2.setGeometry(QRect(30, 220, 151, 31))
        self.email_text_input_2.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.email_text_input_2.setReadOnly(True)
        self.email_div_input_2 = QFrame(self.frame)
        self.email_div_input_2.setObjectName(u"email_div_input_2")
        self.email_div_input_2.setGeometry(QRect(300, 260, 2, 20))
        self.email_div_input_2.setStyleSheet(u"Line{\n"
"background: #ccc}")
        self.email_div_input_2.setFrameShape(QFrame.Shape.VLine)
        self.email_div_input_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.senha_icon = QLabel(self.frame)
        self.senha_icon.setObjectName(u"senha_icon")
        self.senha_icon.setGeometry(QRect(310, 340, 20, 20))
        self.senha_icon.setStyleSheet(u"QLabel{\n"
"background:url(:/login/icons8-cadeado-100.png);\n"
"}\n"
"")
        self.senha_confirm_input = QLineEdit(self.frame)
        self.senha_confirm_input.setObjectName(u"senha_confirm_input")
        self.senha_confirm_input.setGeometry(QRect(30, 330, 311, 41))
        self.senha_confirm_input.setStyleSheet(u"QLineEdit{\n"
"border-radius: 4px;\n"
"border: 1px solid #ccc;\n"
"padding-left:10px;\n"
"font-size:14px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.senha_confirm_input.setEchoMode(QLineEdit.Password)
        self.senha_text_input = QTextEdit(self.frame)
        self.senha_text_input.setObjectName(u"senha_text_input")
        self.senha_text_input.setGeometry(QRect(30, 300, 151, 31))
        self.senha_text_input.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.senha_text_input.setReadOnly(True)
        self.senha_text_input.setTextInteractionFlags(Qt.NoTextInteraction)
        self.senha_div = QFrame(self.frame)
        self.senha_div.setObjectName(u"senha_div")
        self.senha_div.setGeometry(QRect(300, 340, 2, 20))
        self.senha_div.setStyleSheet(u"Line{\n"
"background: #ccc}")
        self.senha_div.setFrameShape(QFrame.Shape.VLine)
        self.senha_div.setFrameShadow(QFrame.Shadow.Sunken)
        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(310, 30, 51, 31))
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/login/icons8-x-40.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(30, 30))
        self.fixed_text = QTextEdit(self.frame)
        self.fixed_text.setObjectName(u"fixed_text")
        self.fixed_text.setGeometry(QRect(30, 70, 281, 51))
        self.fixed_text.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.fixed_text.setStyleSheet(u"QTextEdit{\n"
"background:#FFF\n"
"}")
        self.fixed_text.setReadOnly(True)
        self.fixed_text.setTextInteractionFlags(Qt.NoTextInteraction)
        self.senha_text_input.raise_()
        self.senha_confirm_input.raise_()
        self.email_text_input_2.raise_()
        self.login_text.raise_()
        self.email_text_input.raise_()
        self.email_input.raise_()
        self.cadastrar_button.raise_()
        self.email_div_input.raise_()
        self.email_icon.raise_()
        self.senha_input.raise_()
        self.email_icon_2.raise_()
        self.email_div_input_2.raise_()
        self.senha_icon.raise_()
        self.senha_div.raise_()
        self.close_button.raise_()
        self.fixed_text.raise_()
        self.background_blue = QWidget(Dialog)
        self.background_blue.setObjectName(u"background_blue")
        self.background_blue.setGeometry(QRect(0, 0, 810, 610))
        self.background_blue.setStyleSheet(u"QWidget{\n"
"background:#0265CB\n"
"}")
        self.background_blue.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:696; color:#284658;\">Recupera\u00e7\u00e3o </span></p></body></html>", None))
        self.email_text_input.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696; color:#2d4a5c;\">E-mail</span></p></body></html>", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite seu e-mail", None))
        self.cadastrar_button.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
        self.email_icon.setText("")
        self.senha_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite sua nova senha", None))
        self.email_icon_2.setText("")
        self.email_text_input_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696; color:#2d4a5c;\">Nova Senha</span></p></body></html>", None))
        self.senha_icon.setText("")
        self.senha_confirm_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirme sua nova senha", None))
        self.senha_text_input.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696; color:#2d4a5c;\">Confirme sua senha</span></p></body></html>", None))
        self.close_button.setText("")
        self.fixed_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#666666;\">Digite um email v\u00e1lido para libera\u00e7\u00e3o dos campos de senha</span></p></body></html>", None))
    # retranslateUi

