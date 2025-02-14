from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

import sys
import os 

class main_wnd(QWidget):
    def __init__(self):
        super().__init__()
        
        # Main Wnd 크기 등을 설정
        
        self.setGeometry(100, 100, 600, 600)
        self.setFixedSize(600, 300)
        
        self.ds_set_wmd()
        
        self.show()
    
    def ds_set_wmd(self):
        # Main Wnd에 포함되는 Widgets을 생성 및 추가
        label0 = QLabel('Hello, World 한글테스트', self)
        
        label0.setFont(QFont('Arial', 15))
        label0.setStyleSheet("background-color: yellow")
        label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label0.move(30,30)
        
        self.ds_set_label1()
        self.show()
    
    def ds_set_label1(self):
        
        label1 = QLabel(self)
        pstr = os.path.realpath(__file__)
        pstr = os.path.dirname(pstr)
        istr = os.path.join(pstr, 'C:/Users/goods/OneDrive/사진/simba.jpg')
        
        #pixmap = QPixmap('./img/8.jpg')
        pixmap = QPixmap(istr)
        pixmap = pixmap.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio)
        label1.setPixmap(pixmap)
        label1.setScaledContents(True)
        #label1.setPixmap(QPixmap('./img/8.png'))
        
        label1.move(30,80)
        
        
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

# 내가 만든 Qt 관련 main window 인스턴스를 만들어야함
mw = main_wnd()

sys.exit(app.exec())