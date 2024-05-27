import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class DirectoryViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Directory Viewer")
        self.layout = QVBoxLayout()

        self.directory_list = QListWidget()
        self.populate_directory_list()
        self.layout.addWidget(self.directory_list)

        self.add_button = QPushButton("Add Directory")
        self.add_button.clicked.connect(self.add_directory)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Selected Directory")
        self.delete_button.clicked.connect(self.delete_directory)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def populate_directory_list(self):
        self.directory_list.clear()

        current_path = os.getcwd()
        for item in os.listdir(current_path):
            if os.path.isdir(item):
                self.directory_list.addItem(item)

    def add_directory(self):
        directory_name, is_valid = QInputDialog.getText(self, "Add Directory", "Enter directory name:")

        if is_valid and directory_name:
            try:
                os.mkdir(directory_name)
                self.populate_directory_list()
            except OSError as e:
                QMessageBox.critical(self, "Error", str(e))

    def delete_directory(self):
        selected_item = self.directory_list.currentItem()

        if selected_item:
            directory_name = selected_item.text()
            confirmed = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the directory '{directory_name}'?", QMessageBox.Yes | QMessageBox.No)

            if confirmed == QMessageBox.Yes:
                try:
                    os.rmdir(directory_name)
                    self.populate_directory_list()
                except OSError as e:
                    QMessageBox.critical(self, "Error", str(e))

def main():
    app = QApplication(sys.argv)

    window = DirectoryViewer()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
