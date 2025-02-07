import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt


class NameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Programa maneiro')

        self.label_name = QLabel('Login')
        self.input_name = QLineEdit()


        self.label_senha = QLabel('Senha')
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)


        self.button_check = QPushButton('Login')
        self.button_check.clicked.connect (self.check_login)

    
        self.result_name = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.label_name,alignment=Qt.AlignCenter)
        layout.addWidget(self.input_name,alignment=Qt.AlignCenter)
        layout.addWidget(self.label_senha,alignment=Qt.AlignCenter)
        layout.addWidget(self.input_senha,alignment=Qt.AlignCenter)
        layout.addWidget(self.button_check,alignment=Qt.AlignCenter)
        layout.addWidget(self.result_name,alignment=Qt.AlignCenter)

        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)


    def check_login(self):
        username = self.input_name.text()
        password = self.input_senha.text()

        if username == 'adm' and password == '123':
            self.show_message('Login Valido','Sucesso ao entrar!',QMessageBox.Information)
        else: 
            self.show_message('Login Invalido!','Falha!',QMessageBox.Critical)

    def show_message (self , title, message, icon_type):
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NameWindow()
    window.show()

    sys.exit(app.exec_())