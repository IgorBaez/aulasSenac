# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QMessageBox,
    QStatusBar, QWidget)
import SSSS, CCC, Formulario, sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.janela = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.frame_LOGIN = QFrame(self.centralwidget)
        self.frame_LOGIN.setObjectName(u"frame_LOGIN")
        self.frame_LOGIN.setGeometry(QRect(250, 80, 201, 281))
        self.frame_LOGIN.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.frame_LOGIN.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_LOGIN.setFrameShadow(QFrame.Shadow.Raised)

        self.label_senha = QLabel(self.frame_LOGIN)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(60, 90, 81, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_senha.setFont(font)
        self.label_senha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_login = QLabel(self.frame_LOGIN)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(60, 20, 71, 41))
        self.label_login.setFont(font)
        self.label_login.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_login.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.lineEdit_SENHA = QLineEdit(self.frame_LOGIN)
        self.lineEdit_SENHA.setObjectName(u"lineEdit_SENHA")
        self.lineEdit_SENHA.setGeometry(QRect(40, 140, 113, 22))
        self.lineEdit_SENHA.setEchoMode(QLineEdit.EchoMode.Password)

        self.lineEdit_LOGIN = QLineEdit(self.frame_LOGIN)
        self.lineEdit_LOGIN.setObjectName(u"lineEdit_LOGIN")
        self.lineEdit_LOGIN.setGeometry(QRect(40, 60, 113, 22))

        self.label_IMG = QLabel(self.frame_LOGIN)
        self.label_IMG.setObjectName(u"label_IMG")
        self.label_IMG.setGeometry(QRect(110, 210, 81, 61))
        self.label_IMG.setPixmap(QPixmap(u":/ICON/SSSS.png"))
        self.label_IMG.setScaledContents(True)

        self.Button_ENTRAR = QPushButton(self.frame_LOGIN)
        self.Button_ENTRAR.setObjectName(u"Button_ENTRAR")
        self.Button_ENTRAR.setGeometry(QRect(60, 180, 75, 24))
        self.Button_ENTRAR.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""")
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
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_IMG.setText("")
        self.Button_ENTRAR.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))