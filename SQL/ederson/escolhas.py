# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'escolhas.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Salgados = QWidget()
        self.Salgados.setObjectName(u"Salgados")
        self.verticalLayout_3 = QVBoxLayout(self.Salgados)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.Salgados)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.Salgados)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.Salgados)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.Salgados)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.Salgados, "")
        self.Bebidas = QWidget()
        self.Bebidas.setObjectName(u"Bebidas")
        self.gridLayout = QGridLayout(self.Bebidas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_8 = QFrame(self.Bebidas)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_6.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.Bebidas)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.Bebidas)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.Bebidas)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_8.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Bebidas, "")
        self.Outros = QWidget()
        self.Outros.setObjectName(u"Outros")
        self.gridLayout_2 = QGridLayout(self.Outros)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_13 = QFrame(self.Outros)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.pushButton_12 = QPushButton(self.frame_13)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_13.addWidget(self.pushButton_12)


        self.gridLayout_2.addWidget(self.frame_13, 3, 0, 1, 1)

        self.frame_11 = QFrame(self.Outros)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.gridLayout_2.addWidget(self.frame_11, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.Outros)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_12.addWidget(self.pushButton_11)


        self.gridLayout_2.addWidget(self.frame_12, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.Outros)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_9.addWidget(self.pushButton_9)


        self.gridLayout_2.addWidget(self.frame_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Outros, "")
        self.Carrinho = QWidget()
        self.Carrinho.setObjectName(u"Carrinho")
        self.verticalLayout_2 = QVBoxLayout(self.Carrinho)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.Carrinho)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_14)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listView = QListView(self.frame_14)
        self.listView.setObjectName(u"listView")
        self.listView.setAutoScroll(True)

        self.gridLayout_3.addWidget(self.listView, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.tabWidget.addTab(self.Carrinho, "")

        self.horizontalLayout_14.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Esfirra ....................... R$2,50", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coxinha .................... R$2,50", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Risole ........................ R$2,50", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pizza .......................... R$2,50", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Salgados), QCoreApplication.translate("MainWindow", u"Salgados", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Coca 220ml .......................... R$2,50", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Suco Del Valle .......................... R$2,50", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fanta 220ml  .......................... R$2,50", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Coca 1L ................................ R$2,50", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bebidas), QCoreApplication.translate("MainWindow", u"Bebidas", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pa\u00e7oca ................................ R$2,50", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bala ................................ R$2,50", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Chiclete ................................ R$2,50", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pirulito ................................ R$2,50", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao carrinho", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Outros), QCoreApplication.translate("MainWindow", u"Outros", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Itens do carrinho", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Carrinho), QCoreApplication.translate("MainWindow", u"Carrinho", None))
    # retranslateUi

