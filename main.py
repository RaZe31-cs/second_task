import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Random_Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.clicked_btn)
        self.draw = False
        self.color = QColor(255, 255, 0)
        '''
        Рекомендую self.color присвоить черный цвет QColor(0, 0, 0)
        иначе будет плохо видно круг
        '''

    def clicked_btn(self):
        self.draw = True
        self.repaint()
        self.draw = False

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_smile(qp)
            qp.end()

    def draw_smile(self, qp):
        x0 = random.randrange(0, 850)
        y0 = random.randrange(0, 580)
        radius = random.randrange(0, 200)
        while x0 + radius * 2 > 850 or y0 + radius * 2 > 580:
            x0 = random.randrange(0, 850)
            y0 = random.randrange(0, 580)
        qp.setPen(self.color)
        qp.drawEllipse(x0, y0, radius * 2, radius * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Random_Circle()
    ex.show()
    sys.exit(app.exec())
