import sys
from PySide6.QtWidgets import (QApplication, 
               QMainWindow, QPushButton, 
               QVBoxLayout, QMessageBox)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog.information Example')
        self.setup_main_wnd()
        self.show()
    
    def setup_main_wnd(self):
        lm = QVBoxLayout()
        
        bt01 = QPushButton("QDialog", self)
        bt02 = QPushButton("QMessageBox information", self)
        bt03 = QPushButton("QMessageBox about", self)
        bt04 = QPushButton("QMessageBox question", self)
        bt05 = QPushButton("QMessageBox critical", self)
        bt06 = QPushButton("QMessageBox warning", self)
        bt07 = QPushButton("QMessageBox about", self)
        
        lm.addWidget(bt01)
        lm.addWidget(bt02)
        lm.addWidget(bt03)
        lm.addWidget(bt04)
        lm.addWidget(bt05)
        lm.addWidget(bt06)
        lm.addWidget(bt07)
        
        self.setLayout(lm)
        
        bt01.clicked.connect(self.bt01_clicked)
        bt02.clicked.connect(self.bt02_clicked)
        bt03.clicked.connect(self.bt03_clicked)
        bt04.clicked.connect(self.bt04_clicked)
        bt05.clicked.connect(self.bt05_clicked)
        bt06.clicked.connect(self.bt06_clicked)
        bt07.clicked.connect(self.bt07_clicked)
    
    def bt01_clicked(self, s):
        print("click", s)
        
    def bt02_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)       
        
    def bt03_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)       
    def bt04_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)         
    def bt05_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)      
    def bt06_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)   
    def bt07_clicked(self, s):
        print("click", s)
        result = QMessageBox.information(
            self,                    # parent
            "",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok # 버튼들.
)                  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    app.exec()