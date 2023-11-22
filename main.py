import sys
import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow

class CircleDraw(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go)
        self.ispaint = False

    def go(self):
        self.ispaint = True
        self.update()

    def Draw(self, qp: QPainter):
        color = QColor(random.randint(0, 255),
                        random.randint(0, 255), 
                        random.randint(0, 255))
        radius = random.randint(10, min(self.width(), self.height()) // 2 - 10)
        xPos = random.randrange(0, self.width() - radius)
        yPos = random.randrange(0, self.height() - radius)
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