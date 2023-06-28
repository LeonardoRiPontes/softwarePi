import sys
from PySide6.QtWidgets import QWidget,QApplication

from login_interface import Ui_Form

class Logar(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Logar()
    mainWindow.show()
    sys.exit(app.exec())