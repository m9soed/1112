import sys
from PySide6.QtWidgets import *
# from PySide6.QtGui import QFileInfo
from PySide6.QtCore import Qt, QFileInfo

class FileDialogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("CSV File Info")
        layout = QVBoxLayout()
        
        self.info_text_edit = QTextEdit()
        self.info_text_edit.setReadOnly(True)
        layout.addWidget(self.info_text_edit)
        
        select_file_button = QPushButton("Select CSV File")
        select_file_button.clicked.connect(self.select_file)
        layout.addWidget(select_file_button)
        
        self.setLayout(layout)
    
    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV Files (*.csv)")
        
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            
            if selected_files:
                file_path = selected_files[0]
                file_info = QFileInfo(file_path)
                
                info_text = f"Absolute Path: {file_info.absoluteFilePath()}\n"
                info_text += f"Base Name: {file_info.baseName()}\n"
                
                if file_info.isReadable():
                    info_text += "Can Read: Yes\n"
                else:
                    info_text += "Can Read: No\n"
                
                if file_info.isWritable():
                    info_text += "Can Write: Yes\n"
                else:
                    info_text += "Can Write: No\n"
                
                if file_info.isExecutable():
                    info_text += "Executable: Yes\n"
                else:
                    info_text += "Executable: No\n"
                
                info_text += f"Created: {file_info.birthTime().toString(Qt.ISODate)}\n"
                info_text += f"Last Modified: {file_info.lastModified().toString(Qt.ISODate)}\n"
                
                self.info_text_edit.setPlainText(info_text)

def main():
    app = QApplication(sys.argv)
    
    window = FileDialogApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
