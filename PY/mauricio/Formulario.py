# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Formulario.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_formulario = QLabel(self.centralwidget)
        self.label_formulario.setObjectName(u"label_formulario")
        self.label_formulario.setGeometry(QRect(270, 40, 91, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_formulario.setFont(font)
        self.frame_nome = QFrame(self.centralwidget)
        self.frame_nome.setObjectName(u"frame_nome")
        self.frame_nome.setGeometry(QRect(210, 100, 271, 51))
        self.frame_nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_nome.setFrameShadow(QFrame.Shadow.Raised)
        self.label_nome = QLabel(self.frame_nome)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(0, 0, 49, 16))
        self.lineEdit_nome = QLineEdit(self.frame_nome)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(0, 20, 161, 22))
        self.frame_ender = QFrame(self.centralwidget)
        self.frame_ender.setObjectName(u"frame_ender")
        self.frame_ender.setGeometry(QRect(210, 160, 271, 51))
        self.frame_ender.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ender.setFrameShadow(QFrame.Shadow.Raised)
        self.label_ender = QLabel(self.frame_ender)
        self.label_ender.setObjectName(u"label_ender")
        self.label_ender.setGeometry(QRect(0, 0, 49, 16))
        self.lineEdit_Ender = QLineEdit(self.frame_ender)
        self.lineEdit_Ender.setObjectName(u"lineEdit_Ender")
        self.lineEdit_Ender.setGeometry(QRect(0, 20, 161, 22))
        self.frame_CPF = QFrame(self.centralwidget)
        self.frame_CPF.setObjectName(u"frame_CPF")
        self.frame_CPF.setGeometry(QRect(210, 220, 271, 51))
        self.frame_CPF.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_CPF.setFrameShadow(QFrame.Shadow.Raised)
        self.label_CPF = QLabel(self.frame_CPF)
        self.label_CPF.setObjectName(u"label_CPF")
        self.label_CPF.setGeometry(QRect(0, 0, 49, 16))
        self.lineEdit_CPF = QLineEdit(self.frame_CPF)
        self.lineEdit_CPF.setObjectName(u"lineEdit_CPF")
        self.lineEdit_CPF.setGeometry(QRect(0, 20, 113, 22))
        self.frame_sexo = QFrame(self.centralwidget)
        self.frame_sexo.setObjectName(u"frame_sexo")
        self.frame_sexo.setGeometry(QRect(210, 280, 120, 61))
        self.frame_sexo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sexo.setFrameShadow(QFrame.Shadow.Raised)
        self.radioButton_Feminino = QRadioButton(self.frame_sexo)
        self.radioButton_Feminino.setObjectName(u"radioButton_Feminino")
        self.radioButton_Feminino.setGeometry(QRect(0, 40, 89, 20))
        self.radioButton_Masculino = QRadioButton(self.frame_sexo)
        self.radioButton_Masculino.setObjectName(u"radioButton_Masculino")
        self.radioButton_Masculino.setGeometry(QRect(0, 20, 89, 20))
        self.label_sexo = QLabel(self.frame_sexo)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setGeometry(QRect(0, 0, 49, 16))
        self.frame_Telefone = QFrame(self.centralwidget)
        self.frame_Telefone.setObjectName(u"frame_Telefone")
        self.frame_Telefone.setGeometry(QRect(210, 350, 261, 51))
        self.frame_Telefone.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Telefone.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_Telefone = QLineEdit(self.frame_Telefone)
        self.lineEdit_Telefone.setObjectName(u"lineEdit_Telefone")
        self.lineEdit_Telefone.setGeometry(QRect(0, 20, 113, 22))
        self.label_telefone = QLabel(self.frame_Telefone)
        self.label_telefone.setObjectName(u"label_telefone")
        self.label_telefone.setGeometry(QRect(0, 0, 49, 16))
        self.frame_confirmo = QFrame(self.centralwidget)
        self.frame_confirmo.setObjectName(u"frame_confirmo")
        self.frame_confirmo.setGeometry(QRect(210, 470, 261, 31))
        self.frame_confirmo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_confirmo.setFrameShadow(QFrame.Shadow.Raised)
        self.checkBox_confirmo = QCheckBox(self.frame_confirmo)
        self.checkBox_confirmo.setObjectName(u"checkBox_confirmo")
        self.checkBox_confirmo.setGeometry(QRect(0, 0, 211, 20))
        self.frame_button_concluir = QFrame(self.centralwidget)
        self.frame_button_concluir.setObjectName(u"frame_button_concluir")
        self.frame_button_concluir.setGeometry(QRect(290, 510, 81, 31))
        self.frame_button_concluir.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_button_concluir.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_concluir = QPushButton(self.frame_button_concluir)
        self.pushButton_concluir.setObjectName(u"pushButton_concluir")
        self.pushButton_concluir.setGeometry(QRect(0, 0, 75, 24))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(210, 410, 120, 51))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 111, 16))
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(0, 20, 110, 22))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(180, 30, 331, 521))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_formulario.setText(QCoreApplication.translate("MainWindow", u"Formulario", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_ender.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_CPF.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.lineEdit_CPF.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.radioButton_Feminino.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.radioButton_Masculino.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.label_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.checkBox_confirmo.setText(QCoreApplication.translate("MainWindow", u"Confirmo as informa\u00e7\u00f5es acima", None))
        self.pushButton_concluir.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
    # retranslateUi





