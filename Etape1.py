from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setFixedSize(600,400)
        layout = QVBoxLayout()
