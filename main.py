from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from sort import organise
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FileFlow")
        self.setFixedSize(QSize(700, 500))
        
        button = QPushButton("Ogranise")
        button.setFixedSize(QSize(100,100))
        button.clicked.connect(organise)
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
sys.exit(0)