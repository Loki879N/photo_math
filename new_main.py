import os
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


# Сhange working directory
cur_dir = os.path.dirname(__file__)
os.chdir(cur_dir)


class MyWidget(QMainWindow):
    result = 0
    def __init__(self):
        super().__init__()
        uic.loadUi("src/MainApplication.ui", self)
        self.pushButton.clicked.connect(self.clicked)

    def getCoefficients(self):
        self.coefK = self.coefK.text()
        self.coefZ = self.coefZ.text()

    def solveLinearEquation(self):
        self.result = self.coefK / self.coefZ
        solve = MainWindow(self, self.result)
        solve.show()


class MainWindow(QMainWindow):
    def __init__(self, solve):
        super().__init__()
        uic.loadUi("src/MainWindow.ui", self)
        self.solve = solve
        self.printSolve(self.solve)

    def printSolve(self):
        self.printSolve.setText(self.solve)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
