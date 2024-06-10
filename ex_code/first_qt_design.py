import sys
from PyQt6.QtWidgets import (QApplication,QWidget)
from PyQt6 import uic

root_dir = os.path.dirname(__file__)
 = os.path.join()
forms = uic.loadUiType('first_qt_designer.ui')

class MW (QWidget, forms[0]):

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.setupUi(self)
        self.init_ui()
        self.show()

    def init_ui(self):
        self.pushButton.clicked.connect(self.clk_slot)

    def clk_slot(self):
        self.cnt += 1
        self.label.setText(f"{self.cnt} clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())