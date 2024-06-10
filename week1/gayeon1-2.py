#basic_wondow.py
#Import necessary modules
import sys

py1 = True
try:
    import PySide6.QtCore	
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel)
except:
    py1 = False

py2 = True
try:
    import PyQt6.QtCore
    from PyQt6.QtWidgets import (QApplication, QWidget, QLabel)

except:
    py2 = False

class MW(QWidget):  #QWidget은 container 역할을 하는 Main Window -> 얘는 여러개 생성 ㄱㄴ / Main Window는 1개만 ㄱㄴ
    def __init__(self):
        """ Constructer for Empty Window Class """
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        """set up the application."""
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("")
        self.setup_main_wnd()
        self.show() #display the window on the screen

    def setup_main_wnd(self):
         """set up the main window."""
         hello_label = QLabel(self)
         hello_label.setText('')
         hello_label.move(150,90)
#run the program
if __name__ == '__main__' :

    if py1:
        print(PySide6.__version__)
        print(PySide6.QtCore.__version__)
    if py2:
        print(PyQt6.QtCore.qVersion())
   
    app = QApplication(sys.argv) #01 어플리케이션 생성
    window = MW()
    sys.exit(app.exec())

    print(sys.argv)
    
  