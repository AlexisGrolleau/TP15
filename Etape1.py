from PySide2.QtWidgets import *
from PySide2.QtGui import *

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setFixedSize(600,400)
        layout = QVBoxLayout()
        self.setLayout(layout)
        mybutton = ButtonsPanel()
        layout.addWidget(mybutton)

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        configbutton = QPushButton("Configure")
        connectbutton = QPushButton("Connect")
        disconnectbutton = QPushButton("Disconnect")
        layout.addWidget(configbutton)
        layout.addWidget(connectbutton)
        layout.addWidget(disconnectbutton)
        self.setLayout(layout)


if __name__ == "__main__":
   app = QApplication([])
   win = SQLClientWindow()
   win.show()
   app.exec_()
