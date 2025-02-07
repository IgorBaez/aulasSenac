from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Foto e Nome")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Criando um rótulo com o nome
        label = QLabel("Test do Bazzz", self)
        label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        label.setAlignment(Qt.AlignCenter)

        # Criando um rótulo para a imagem
        img_label = QLabel(self)
        pixmap = QPixmap("cat.jpg")
        pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)

        # Adicionando widgets ao layout
        layout.addWidget(label)
        layout.addWidget(img_label)

        # Definindo o widget central
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameWindow()
    window.show()
    sys.exit(app.exec())