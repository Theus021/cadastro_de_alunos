# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_home-Copia.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)
import telas.principal_rc
import telas.toolBar_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.text_header = QPushButton(self.widget)
        self.text_header.setObjectName(u"text_header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_header.sizePolicy().hasHeightForWidth())
        self.text_header.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.text_header.setFont(font)
        self.text_header.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.text_header.setStyleSheet(u"QPushButton{\n"
"background:#0265CB;\n"
"border:none;\n"
"padding: 0px 0xp 0px 5px;\n"
"font-size: 16px;\n"
"color: #FFF;\n"
"}")
        self.text_header.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.text_header)

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
        icon.addFile(u":/principal/setting (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.config_button_bar.setIcon(icon)
        self.config_button_bar.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.config_button_bar)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 70, 981, 511))
        self.widget_3.setStyleSheet(u"")
        self.search_icon = QLabel(self.widget_3)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(50, 160, 30, 31))
        self.search_icon.setStyleSheet(u"QLabel{\n"
"image: url(:/principal/icon_pesquisa.png);\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.filtro_por_QcomboBox = QComboBox(self.widget_3)
        self.filtro_por_QcomboBox.addItem("")
        self.filtro_por_QcomboBox.addItem("")
        self.filtro_por_QcomboBox.addItem("")
        self.filtro_por_QcomboBox.addItem("")
        self.filtro_por_QcomboBox.addItem("")
        self.filtro_por_QcomboBox.setObjectName(u"filtro_por_QcomboBox")
        self.filtro_por_QcomboBox.setGeometry(QRect(620, 160, 151, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.filtro_por_QcomboBox.setFont(font1)
        self.filtro_por_QcomboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.filtro_por_QcomboBox.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
        self.search_input = QLineEdit(self.widget_3)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setGeometry(QRect(40, 160, 401, 31))
        self.search_input.setStyleSheet(u"QLineEdit{\n"
"font-size:16px;\n"
"background: #F7F8FC;\n"
"padding-left: 45px;\n"
"border-radius: 3px;\n"
"transition: border 0.2s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid #c2dbfe\n"
"}")
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 981, 511))
        self.frame.setStyleSheet(u"QFrame{\n"
"background: #FFF;\n"
"border-radius: 10px;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.div_grey = QLabel(self.frame)
        self.div_grey.setObjectName(u"div_grey")
        self.div_grey.setGeometry(QRect(40, 120, 900, 2))
        self.div_grey.setStyleSheet(u"QLabel{\n"
"background: #CCC;\n"
"border-radius 5px}")
        self.alunos_div_tg = QLabel(self.frame)
        self.alunos_div_tg.setObjectName(u"alunos_div_tg")
        self.alunos_div_tg.setGeometry(QRect(160, 120, 90, 2))
        self.alunos_div_tg.setStyleSheet(u"QLabel{\n"
"background: #CCC;\n"
"border-radius 5px}")
        self.prof_div_tg = QLabel(self.frame)
        self.prof_div_tg.setObjectName(u"prof_div_tg")
        self.prof_div_tg.setGeometry(QRect(290, 120, 110, 2))
        self.prof_div_tg.setStyleSheet(u"QLabel{\n"
"background: #CCC;\n"
"border-radius 5px}")
        self.professores_tg = QPushButton(self.frame)
        self.professores_tg.setObjectName(u"professores_tg")
        self.professores_tg.setGeometry(QRect(290, 90, 111, 23))
        self.professores_tg.setFont(font1)
        self.professores_tg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.professores_tg.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: #B1B2B3\n"
"}")
        self.alunos_tg = QPushButton(self.frame)
        self.alunos_tg.setObjectName(u"alunos_tg")
        self.alunos_tg.setGeometry(QRect(160, 90, 91, 23))
        self.alunos_tg.setFont(font1)
        self.alunos_tg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.alunos_tg.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: #B1B2B3\n"
"}")
        self.alunos_tg.setCheckable(False)
        self.alunos_tg.setChecked(False)
        self.todos_div_tg = QLabel(self.frame)
        self.todos_div_tg.setObjectName(u"todos_div_tg")
        self.todos_div_tg.setGeometry(QRect(40, 120, 90, 2))
        self.todos_div_tg.setStyleSheet(u"QLabel{\n"
"background: #0265CB;\n"
"border-radius 5px}")
        self.todos_Tg = QPushButton(self.frame)
        self.todos_Tg.setObjectName(u"todos_Tg")
        self.todos_Tg.setGeometry(QRect(40, 90, 91, 23))
        self.todos_Tg.setFont(font1)
        self.todos_Tg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.todos_Tg.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: #0265CB\n"
"}")
        self.list_text_header = QLabel(self.frame)
        self.list_text_header.setObjectName(u"list_text_header")
        self.list_text_header.setGeometry(QRect(40, 20, 191, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.list_text_header.setFont(font2)
        self.list_text_header.setStyleSheet(u"QLabel{\n"
"color: #081452}")
        self.tableWidget_2 = QTableWidget(self.frame)
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
        self.tableWidget_2.setGeometry(QRect(40, 180, 901, 301))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"border-radius: 3px;\n"
"\n"
"alternate-background-color: #F7F8FC;\n"
"background-color: white;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border: none;\n"
"background: #FFF;\n"
"border-bottom: 2px solid #808BBF;\n"
"color: #99A2CC;\n"
"padding: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"border-bottom: 1px solid #CCC;\n"
"color: #000;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 5px;  \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical {\n"
"    background: #888;\n"
"    min-height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #555;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #333;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: n"
                        "one;\n"
"}\n"
"")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setTextElideMode(Qt.ElideLeft)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setGridStyle(Qt.NoPen)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(42)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.adicionar_button = QPushButton(self.widget_3)
        self.adicionar_button.setObjectName(u"adicionar_button")
        self.adicionar_button.setGeometry(QRect(740, 40, 201, 41))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.adicionar_button.setFont(font3)
        self.adicionar_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.adicionar_button.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/principal/icon_soma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.adicionar_button.setIcon(icon1)
        self.adicionar_button.setIconSize(QSize(30, 30))
        self.ordenar_por_QcomboBox = QComboBox(self.widget_3)
        self.ordenar_por_QcomboBox.addItem("")
        self.ordenar_por_QcomboBox.addItem("")
        self.ordenar_por_QcomboBox.addItem("")
        self.ordenar_por_QcomboBox.addItem("")
        self.ordenar_por_QcomboBox.setObjectName(u"ordenar_por_QcomboBox")
        self.ordenar_por_QcomboBox.setGeometry(QRect(790, 160, 151, 31))
        self.ordenar_por_QcomboBox.setFont(font1)
        self.ordenar_por_QcomboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ordenar_por_QcomboBox.setStyleSheet(u"QComboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 3px;\n"
"padding-left:15px;\n"
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
        self.frame.raise_()
        self.filtro_por_QcomboBox.raise_()
        self.search_input.raise_()
        self.search_icon.raise_()
        self.adicionar_button.raise_()
        self.ordenar_por_QcomboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_header.setText(QCoreApplication.translate("MainWindow", u" Tech School", None))
        self.config_button_bar.setText(QCoreApplication.translate("MainWindow", u" Configura\u00e7\u00e3o", None))
        self.search_icon.setText("")
        self.filtro_por_QcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Turma", None))
        self.filtro_por_QcomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ads", None))
        self.filtro_por_QcomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Data-science", None))
        self.filtro_por_QcomboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Machine-learning", None))
        self.filtro_por_QcomboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Software-engineer", None))

        self.search_input.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome a ser pesquisado", None))
        self.div_grey.setText("")
        self.alunos_div_tg.setText("")
        self.prof_div_tg.setText("")
        self.professores_tg.setText(QCoreApplication.translate("MainWindow", u"Professores", None))
        self.alunos_tg.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.todos_div_tg.setText("")
        self.todos_Tg.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.list_text_header.setText(QCoreApplication.translate("MainWindow", u"Lista De :", None))
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
        self.adicionar_button.setText(QCoreApplication.translate("MainWindow", u" Add novo registro", None))
        self.ordenar_por_QcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar Por ", None))
        self.ordenar_por_QcomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.ordenar_por_QcomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CPF", None))
        self.ordenar_por_QcomboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Turma", None))

    # retranslateUi

