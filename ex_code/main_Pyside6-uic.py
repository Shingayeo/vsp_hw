import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

from Pyside6_uic_test import Ui_MainWindow # 변환된 UI 모듈(from 내가 정한 파일 이름)

class MW(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineEdit.returnPressed.connect(self.my_slot)   
        self.show()
        
    def my_slot(self):
        c_text = self.lineEdit.text()
        self.label.setText(c_text)
        
                   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
    