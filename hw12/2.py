import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QTextLayout, QTextOption, QPainter, QFont, QPen, QColor
from PySide6.QtCore import Qt, QPoint, QRectF

class TextWithLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text with QTextLayout and Shapes")
        self.setGeometry(100, 100, 600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Рисуем полукольцо слева от текста
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.blue)
        painter.drawChord(50, 50, 100, 300, 0, 180 * 16)

        # Рисуем полукольцо справа от текста
        painter.setBrush(Qt.red)
        painter.drawChord(self.width() - 150, 50, 100, 300, 0, -180 * 16)

        text = "Пример текста с помощью QTextLayout"

        layout = QTextLayout(text)
        layout.setFont(QFont("Arial", 12))  # Установка шрифта и размера шрифта
        layout.setTextOption(QTextOption(Qt.AlignCenter))  # Выравнивание текста по центру

        # Установка цвета текста
        pen = QPen(QColor(Qt.white))
        painter.setPen(pen)

        layout.beginLayout()
        textRect = layout.createLine()
        textRect.setLeadingIncluded(True)
        layout.endLayout()

        x_offset = (self.width() - layout.boundingRect().width()) / 2
        y_offset = (self.height() - layout.boundingRect().height()) / 2

        painter.translate(x_offset, y_offset)
        layout.draw(painter, QPoint(0, 0))

def main():
    app = QApplication(sys.argv)
    window = TextWithLayout()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
