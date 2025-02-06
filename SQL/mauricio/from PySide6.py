from PySide6.QtCore import QApplication, Qlabel, QMainWindonw, QVBoxLayout, QWidget, Qt
from PySide6.QtGui import QPixmap 
import sys

class NameWindow(QMainWindonw):
    def __init__(self):
        super().__init__()
        self.setWindoTitle("foto e nome")
        self.setGeometry(100,100,400,400)

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)

        label=Qlabel("Professor Bazzz",self)
        label.setStyleSheet("font-size:24px; font-weight: bold; text-align:center")
        label.setAlignment(Qt.aligmCenter)

        img_label=Qlabel(self)
        pixmap = QPixmap("foto.png")
        pixmap = pixmap.scaled(200, 200)
        img_label.setPixmap(pixmap)

        layout.addWidget(label)
        layout.addwidgat(img_label)
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    
    window = NameWindow()
    window.show()

    sys.exit(app.exec())




