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

        label = QLabel("Professor Bazzz", self)
        label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 10px;")
        label.setAlignment(Qt.AlignCenter)

        img_label = QLabel(self)
        pixmap = QPixmap("cat.jpg")
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        img_label.setPixmap(pixmap)
       

        layout.addWidget(label)
        layout.addWidget(img_label)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameWindow()
    window.show()
    sys.exit(app.exec())
