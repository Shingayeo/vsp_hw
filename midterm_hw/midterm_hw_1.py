import sys, os
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, 
                               QVBoxLayout)

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(200,100,300,200)
        
        layout = QVBoxLayout() # 출력 위치가 너무 보기 불편해서 추가
        label = QLabel("Hello, World")
        layout.addWidget(label)
        
        self.setLayout(layout)
        
        self.show()
       
if __name__ == "__main__":
    dir = os.path.dirname(os.path.realpath(__file__))
    print("현재 main script의 디렉토리 경로:", dir)
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
    
    