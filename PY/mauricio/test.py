from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QIntValidator
from PyQt6 import QtWidgets

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Validador de Senha")
        MainWindow.resize(400, 200)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.input_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.input_senha.setGeometry(50, 50, 300, 30)
        self.input_senha.setPlaceholderText("Digite a senha")
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Esconde os caracteres

        self.botao_validar = QtWidgets.QPushButton("Validar Senha", self.centralwidget)
        self.botao_validar.setGeometry(150, 100, 100, 30)
        self.botao_validar.clicked.connect(self.validar_senha)

    def validar_senha(self):
        senha = self.input_senha.text()

        if len(senha) < 8:
            QMessageBox.warning(None, "Erro", "A senha deve ter pelo menos 8 caracteres!")
        elif not any(c.isdigit() for c in senha):
            QMessageBox.warning(None, "Erro", "A senha deve conter pelo menos um número!")
        elif not any(c.isupper() for c in senha):
            QMessageBox.warning(None, "Erro", "A senha deve conter pelo menos uma letra maiúscula!")
        else:
            QMessageBox.information(None, "Sucesso", "Senha válida!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
