from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QMessageBox,
    QStatusBar, QWidget)
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Login import Ui_MainWindow
from Formulario import Uie_MainWindows



DB_HOST = "127.0.0.1"  
DB_USER = "root"       
DB_PASSWORD = ""
DB_NAME = ""


USUARIO_CORRETO = "bazz"
SENHA_CORRETA = "123"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login=Ui_MainWindow()
        self.login.setupUi(self)
        self.centralizar_login()

        # Conectar o botão ao método de login
        self.login.Button_ENTRAR.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.login.lineEdit_LOGIN.text()
        senha = self.login.lineEdit_SENHA.text()

        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            QMessageBox.information(None, "Sucesso", "Login bem-sucedido!")
            self.abrir_tela_principal()
        else:
            QMessageBox.warning(None, "Erro", "Usuário ou senha incorretos!")
    
    def resizeEvent(self, event):
        """Recentraliza o login sempre que a janela for redimensionada."""
        self.centralizar_login()
        super().resizeEvent(event)

    def centralizar_login(self):
        """Centraliza o frame de login na tela."""
        largura_janela = self.width()  # Corrigido: 'self.janela' não existe, usar 'self'
        altura_janela = self.height()
        largura_frame = self.login.frame_LOGIN.width()
        altura_frame = self.login.frame_LOGIN.height()

        pos_x = (largura_janela - largura_frame) // 2
        pos_y = (altura_janela - altura_frame) // 2

        self.login.frame_LOGIN.setGeometry(pos_x, pos_y, largura_frame, altura_frame)


    
    def abrir_tela_principal(self):
        self.login.janela.close()  # Fecha a janela de login
        self.janela_formulario = QMainWindow()
        self.formulario = Uie_MainWindows()  # Supondo que Formulario tenha uma classe Ui_MainWindow
        self.formulario.setupUi(self.janela_formulario)
        self.janela_formulario.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()  
    sys.exit(app.exec())

