# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_home.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import telas.principal_rc
import telas.toolBar_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 601)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 50, 1020, 150))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background: #03A9F4;\n"
"}")
        self.nome_tabela_label = QLabel(self.widget_2)
        self.nome_tabela_label.setObjectName(u"nome_tabela_label")
        self.nome_tabela_label.setGeometry(QRect(60, 50, 891, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.nome_tabela_label.setFont(font)
        self.nome_tabela_label.setStyleSheet(u"QLabel{\n"
"color: #404655;\n"
"background: #F7F7F7;\n"
"}\n"
"")
        self.nome_tabela_label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1020, 51))
        self.widget.setStyleSheet(u"QWidget{\n"
"background:#0265CB\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.config_button_bar_2 = QPushButton(self.widget)
        self.config_button_bar_2.setObjectName(u"config_button_bar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_button_bar_2.sizePolicy().hasHeightForWidth())
        self.config_button_bar_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.config_button_bar_2.setFont(font1)
        self.config_button_bar_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.config_button_bar_2.setStyleSheet(u"QPushButton{\n"
"background:#0265CB;\n"
"border:none;\n"
"padding: 0px 0xp 0px 5px;\n"
"font-size: 16px;\n"
"color: #FFF;\n"
"}")
        self.config_button_bar_2.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.config_button_bar_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.config_button_bar = QPushButton(self.widget)
        self.config_button_bar.setObjectName(u"config_button_bar")
        sizePolicy.setHeightForWidth(self.config_button_bar.sizePolicy().hasHeightForWidth())
        self.config_button_bar.setSizePolicy(sizePolicy)
        self.config_button_bar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.config_button_bar.setStyleSheet(u"QPushButton{\n"
"background:#0265CB;\n"
"border:none;\n"
"padding: 0px 0xp 0px 5px;\n"
"font-size: 16px;\n"
"color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: #EBE9E9\n"
"}")
        icon = QIcon()
        icon.addFile(u":/tool_bar/icons8-configura\u00e7\u00e3o-18 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.config_button_bar.setIcon(icon)
        self.config_button_bar.setIconSize(QSize(17, 16))

        self.horizontalLayout.addWidget(self.config_button_bar)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(60, 140, 891, 411))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"background:#F5F5F5;\n"
"border: 1px solid #CCC;\n"
"}")
        self.search_icon = QLabel(self.widget_3)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(20, 55, 30, 31))
        self.search_icon.setStyleSheet(u"QLabel{\n"
"image: url(:/principal/icons8-pesquisar-20 (1).png);\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.buscar_input = QPushButton(self.widget_3)
        self.buscar_input.setObjectName(u"buscar_input")
        self.buscar_input.setGeometry(QRect(510, 20, 191, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.buscar_input.setFont(font2)
        self.buscar_input.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buscar_input.setStyleSheet(u"QPushButton{\n"
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
"border: 3px solid #CCC}")
        self.buscar_input.setCheckable(False)
        self.buscar_input.setAutoExclusive(False)
        self.editarr_button = QPushButton(self.widget_3)
        self.editarr_button.setObjectName(u"editarr_button")
        self.editarr_button.setGeometry(QRect(730, 11, 151, 81))
        self.editarr_button.setFont(font2)
        self.editarr_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editarr_button.setStyleSheet(u"QPushButton{\n"
"background: #03A9F4;\n"
"color: #FFF;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #18B7FF;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"border: 3px solid #CCC\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/principal/icons8-soma-20.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editarr_button.setIcon(icon1)
        self.editarr_button.setIconSize(QSize(30, 30))
        self.tableWidget_2 = QTableWidget(self.widget_3)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 100, 711, 300))
        self.tableWidget_2.setFont(font1)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"background:#FFF;}")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 11, 711, 81))
        self.label.setStyleSheet(u"QLabel{\n"
"background: #FFF;\n"
"border:none}")
        self.adicionar_aluno_button = QPushButton(self.widget_3)
        self.adicionar_aluno_button.setObjectName(u"adicionar_aluno_button")
        self.adicionar_aluno_button.setGeometry(QRect(730, 310, 151, 41))
        self.adicionar_aluno_button.setFont(font2)
        self.adicionar_aluno_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.adicionar_aluno_button.setStyleSheet(u"QPushButton{\n"
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
"border: 3px solid #CCC}")
        self.adicionar_aluno_button.setIcon(icon1)
        self.adicionar_aluno_button.setIconSize(QSize(30, 30))
        self.adicionar_prof_button = QPushButton(self.widget_3)
        self.adicionar_prof_button.setObjectName(u"adicionar_prof_button")
        self.adicionar_prof_button.setGeometry(QRect(730, 359, 151, 41))
        self.adicionar_prof_button.setFont(font2)
        self.adicionar_prof_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.adicionar_prof_button.setStyleSheet(u"QPushButton{\n"
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
"border: 3px solid #CCC}")
        self.adicionar_prof_button.setIcon(icon1)
        self.adicionar_prof_button.setIconSize(QSize(30, 30))
        self.filtro_comboBox = QComboBox(self.widget_3)
        self.filtro_comboBox.addItem("")
        self.filtro_comboBox.addItem("")
        self.filtro_comboBox.setObjectName(u"filtro_comboBox")
        self.filtro_comboBox.setGeometry(QRect(510, 55, 191, 31))
        self.filtro_comboBox.setFont(font2)
        self.filtro_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.filtro_comboBox.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:10px;\n"
"background: #fff;\n"
"transition: border 0.2s ease-in-out;\n"
"color: #727474;\n"
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
        self.search_input = QLineEdit(self.widget_3)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setGeometry(QRect(20, 55, 471, 31))
        self.search_input.setStyleSheet(u"QLineEdit{\n"
"font-size:16px;\n"
"background: #FFFFFF;\n"
"padding-left: 35px;\n"
"border-radius: 3px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.label.raise_()
        self.buscar_input.raise_()
        self.editarr_button.raise_()
        self.tableWidget_2.raise_()
        self.adicionar_aluno_button.raise_()
        self.adicionar_prof_button.raise_()
        self.filtro_comboBox.raise_()
        self.search_input.raise_()
        self.search_icon.raise_()
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nome_tabela_label.setText(QCoreApplication.translate("MainWindow", u"Tech School", None))
        self.config_button_bar_2.setText(QCoreApplication.translate("MainWindow", u" Tech School", None))
        self.config_button_bar.setText(QCoreApplication.translate("MainWindow", u"  Configura\u00e7\u00e3o", None))
        self.search_icon.setText("")
        self.buscar_input.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.editarr_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome completo", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cpf", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Periodo", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"a\u00e7\u00f5es", None));
        self.label.setText("")
        self.adicionar_aluno_button.setText(QCoreApplication.translate("MainWindow", u"Aluno", None))
        self.adicionar_prof_button.setText(QCoreApplication.translate("MainWindow", u"Professor", None))
        self.filtro_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.filtro_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Professores", None))

        self.search_input.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome a ser pesquisado", None))
    # retranslateUi

