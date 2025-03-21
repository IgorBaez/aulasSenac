# -*- coding: utf-8 -*-
# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from cadastro import Ui_MainWindow as Ui_Cadastro
from escolhas import Ui_MainWindow as Ui_Escolhas

class CadastroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        self.escolhas_window = None  # Referência para a janela de escolhas
        # Conectar o botão "Cadastrar" à função que abre a tela de escolhas
        self.ui.pushButton.clicked.connect(self.abrir_escolhas)

    def abrir_escolhas(self):
        if self.escolhas_window is None:
            self.escolhas_window = EscolhasWindow()
        self.escolhas_window.show()
        self.hide()  # Opcional: esconde a tela de cadastro ao abrir a de escolhas

class EscolhasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Escolhas()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Inicia com a tela de cadastro
    cadastro_window = CadastroWindow()
    cadastro_window.show()
    sys.exit(app.exec())