import sys
import io
import random
from PyQt5 import QtGui, uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor

class CircleDraw(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.FileIO('UI.ui')
        uic.loadUi(f, self) 
        self.pushButton.clicked.connect(self.go)
        self.ispaint = False

    def go(self):
        self.ispaint = True
        self.update()

    def Draw(self, qp: QPainter):
        color = QColor(255, 255, 0)
        radius = random.randint(10, min(self.width(), self.height()) // 2 - 10)
        xPos = random.randrange(radius, self.width() - radius)
        yPos = random.randrange(radius, self.height() - radius)
        qp.setBrush(color)
        qp.drawEllipse(xPos, yPos, radius, radius)

    def paintEvent(self, a0) -> None:
        if self.ispaint:
            qp = QPainter()
            qp.begin(self)
            self.Draw(qp)
            qp.end()

if __name__ == "__main__":
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    sys._excepthook = sys.excepthook
    app = QApplication(sys.argv)
    w = CircleDraw()
    w.show()
    sys.exit(app.exec())