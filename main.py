import os
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


# Сhange working directory
cur_dir = os.path.dirname(__file__)
os.chdir(cur_dir)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/MainApplication.ui", self)
        self.pushButton.clicked.connect(self.clicked)

    def getCoefficients(self):
        self.coefK = self.coefK.text()
        self.coefZ = self.coefZ.text()

    def solveLinearEquation(self):
        self.result = self.coefK / self.coefZ
        solve = self.MainWindow.printSolve()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(MyWidget)
        uic.loadUi("src/MainWindow.ui", self)

    def printSolve(self):
        return self.printSolve.setText(self.result)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
