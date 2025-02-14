import sys, os
import traceback


from PySide6.QtWidgets import (QApplication, QWidget, 
                                   QLabel, QPushButton)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize
    
class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Set up the application's GUI"""
        self.setFixedSize(250,250)
        self.setWindowTitle('QPushButton Example')
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        """Set up the Main Window"""
        
        # hello_label = QLabel("Hello, World and Qt!", self) # 아래 두 라인과 
        self.hello_label = QLabel(self)
        self.hello_label.setText('Hello, World and Qt!')
        self.hello_label.setFont(QFont('Arial',15))
        
        # 아래 두 줄을 주석해제하여 동작을 확인해 볼것.
        # hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        # hello_label.setStyleSheet("background-color: yellow")
        self.hello_label.move(10,20)

        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'C:/Users/goods/OneDrive/사진/지민.jpg')
        
        it_button = QPushButton("icon and text button",self)
        it_button.setIcon(QIcon(img_fstr))
        it_button.clicked.connect(self.it_btn_clicked)
        it_button.resize(150,50)
        it_button.move(50,70)

        icon_button = QPushButton(self)
        icon_button.setIcon(QIcon(img_fstr))
        icon_button.clicked.connect(self.icon_btn_clicked)
        icon_button.setIconSize (QSize(120,30))
        icon_button.resize(150,50)
        icon_button.move(50,130)
        
        text_button = QPushButton("text button",self)
        text_button.clicked.connect(self.text_btn_clicked) 
        text_button.resize(150,50)
        text_button.move(50,190)
         
    def it_btn_clicked(self):
        self.hello_label.setText("지민이는")

    def icon_btn_clicked(self):
        self.hello_label.setText("정말")

    def text_btn_clicked(self):
        self.hello_label.setText("슬픕니다!")    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())