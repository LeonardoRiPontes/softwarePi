import sys
from PySide6.QtWidgets import QMainWindow,QApplication

from interface_login_encontreme import Ui_MainWindow

class Logar(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.logar)

    def logar(self):
        if self.lineEdit_2.text()=="123":
            print("logado")
        else:
            print("Senha Invalida")

class IntPrincipal(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class IntAdmin(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Logar()
    mainWindow.show()
    sys.exit(app.exec())

