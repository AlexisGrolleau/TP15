from PySide2.QtWidgets import *
from PySide2.QtGui import *

class LabeledTextField(QWidget):
    def __init__(self,texte):
        QWidget.__init__(self)
        self.setWindowTitle("Configuration")
        layout = QHBoxLayout()
        lab = QLabel(texte)
        text = QTextEdit()
        layout.addWidget(lab)
        layout.addWidget(text)
        self.setLayout(layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        ip = LabeledTextField("Ip address")
        user = LabeledTextField("User")
        password = LabeledTextField("Password")

if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win.show()
   app.exec_()
