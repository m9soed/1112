"""https://doc.qt.io/qtforpython-6/examples/example_widgets_richtext_orderform.html"""

from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QFont, QTextCharFormat, QTextCursor, QTextFrameFormat, QTextLength, QTextTableFormat
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QTextBrowser, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.letters = QTabWidget()
        self.setCentralWidget(self.letters)
        self.setWindowTitle("Order Form")

    def create_letter(self, name, address, orderItems, sendOffers):
        editor = QTextEdit()
        tab_index = self.letters.addTab(editor, name)
        self.letters.setCurrentIndex(tab_index)

        cursor = editor.textCursor()
        cursor.movePosition(QTextCursor.Start)
        top_frame = cursor.currentFrame()
        top_frame_format = top_frame.frameFormat()
        top_frame_format.setPadding(16)
        top_frame.setFrameFormat(top_frame_format)

        text_format = QTextCharFormat()
        bold_format = QTextCharFormat()
        bold_format.setFontWeight(QFont.Bold)

        reference_frame_format = QTextFrameFormat()
        reference_frame_format.setBorder(1)
        reference_frame_format.setPadding(8)
        reference_frame_format.setPosition(QTextFrameFormat.FloatRight)
        reference_frame_format.setWidth(QTextLength(QTextLength.PercentageLength, 40))
        cursor.insertFrame(reference_frame_format)

        cursor.insertText("A company", bold_format)
        cursor.insertBlock()
        cursor.insertText("321 City Street")
        cursor.insertBlock()
        cursor.insertText("Industry Park")
        cursor.insertBlock()
        cursor.insertText("Another country")

        cursor.setPosition(top_frame.lastPosition())

        cursor.insertText(name, text_format)
        for line in address.split("\n"):
            cursor.insertBlock()
            cursor.insertText(line)

        cursor.insertBlock()
        cursor.insertBlock()

        date = QDate.currentDate()
        date_str = date.toString('d MMMM yyyy')
        cursor.insertText(f"Date: {date_str}", text_format)
        cursor.insertBlock()

        body_frame_format = QTextFrameFormat()
        body_frame_format.setWidth(QTextLength(QTextLength.PercentageLength, 100))
        cursor.insertFrame(body_frame_format)

        cursor.insertText("I would like to place an order for the following "
                "items:", text_format)
        cursor.insertBlock()
        cursor.insertBlock()

        order_table_format = QTextTableFormat()
        order_table_format.setAlignment(Qt.AlignHCenter)
        order_table = cursor.insertTable(1, 2, order_table_format)

        order_frame_format = cursor.currentFrame().frameFormat()
        order_frame_format.setBorder(1)
        cursor.currentFrame().setFrameFormat(order_frame_format)

        cursor = order_table.cellAt(0, 0).firstCursorPosition()
        cursor.insertText("Product", bold_format)
        cursor = order_table.cellAt(0, 1).firstCursorPosition()
        cursor.insertText("Quantity", bold_format)

        for text, quantity in orderItems:
            row = order_table.rows()

            order_table.insertRows(row, 1)
            cursor = order_table.cellAt(row, 0).firstCursorPosition()
            cursor.insertText(text, text_format)
            cursor = order_table.cellAt(row, 1).firstCursorPosition()
            cursor.insertText(str(quantity), text_format)

        cursor.setPosition(top_frame.lastPosition())

        cursor.insertBlock()

        cursor.insertText("Please update my records to take account of the "
                "following privacy information:")
        cursor.insertBlock()

        offers_table = cursor.insertTable(2, 2)

        cursor = offers_table.cellAt(0, 1).firstCursorPosition()
        cursor.insertText("I want to receive more information about your "
                "company's products and special offers.", text_format)
        cursor = offers_table.cellAt(1, 1).firstCursorPosition()
        cursor.insertText("I do not want to receive any promotional "
                "information from your company.", text_format)

        if sendOffers:
            cursor = offers_table.cellAt(0, 0).firstCursorPosition()
        else:
            cursor = offers_table.cellAt(1, 0).firstCursorPosition()

        cursor.insertText('X', bold_format)

        cursor.setPosition(top_frame.lastPosition())
        cursor.insertBlock()
        cursor.insertText("Sincerely,", text_format)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText(name)

    def create_sample(self):
        order_items = [("T-shirt", 5), ("Badge", 6), ("Reference book", 1), ("Coffee cup", 8)]
        self.create_letter('Mr Smith',
                '12 High Street\nSmall Town\nThis country',
                order_items, True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.resize(640, 480)
    window.show()
    window.create_sample()
    app.exec()
