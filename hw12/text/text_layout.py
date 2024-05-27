from PySide6.QtCore import QPointF, QPoint, QRectF
from PySide6.QtGui import Qt, QTextLayout, QFontMetrics, QFont, QPainter, QBrush, QPen, QColor, QPaintEvent
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(700)

    def paintEvent(self, event: QPaintEvent):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        font = QFont("Times", 20, QFont.Bold)
        textLayout = QTextLayout(text, font)
        margin = 10
        radius = min(self.width()/2.0, self.height()/2.0) - margin
        fm = QFontMetrics(font)
        lineHeight = fm.height()
        y = 0
        textLayout.beginLayout()
        while 1:
            # create a new line
            line = textLayout.createLine()
            if not line.isValid():
                break
            x1 = max(0.0, abs(radius**2-(radius-y)**2) ** 0.5)
            x2 = max(0.0, abs(radius**2-(radius-(y+lineHeight))**2) ** 0.5)
            x = max(x1, x2) + margin
            lineWidth = (self.width() - margin) - x
            line.setLineWidth(lineWidth)
            line.setPosition(QPointF(x, margin+y))
            y += line.height()

        textLayout.endLayout()
        painter = QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.white)
        painter.setBrush(QBrush(Qt.black))
        painter.setPen(QPen(Qt.black))
        textLayout.draw(painter, QPoint(0,0))
        painter.setBrush(QBrush(QColor("#a6ce39")))
        painter.setPen(QPen(Qt.black))
        painter.drawEllipse(QRectF(-radius, margin, 2*radius, 2*radius))
        painter.end()



if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()




