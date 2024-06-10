import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QLineEdit, QInputDialog)

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        
        layout = QVBoxLayout()
        tmp = QWidget()
        tmp.setLayout(layout)
        
        
        self.l_buttons = ['getText', 'getMultilineText', 'getint']
        for idx, c_str in enumerate(self.l_buttons):
            button0 = QPushButton(c_str)
            button0.clicked.connect(self.slot00)
            layout.addWidget(button0)
            
        self.ret_label = QLabel()
        layout.addWidget(self.ret_label)
        
        self.setCentralWidget(tmp)


    def slot00(self):
        print(self.sender())
        sender = self.sender()

        tmp_str = sender.text()
        
        is_ok = False
        
        if tmp_str == self.l_buttons[0]:
            ret_val, is_ok = QInputDialog.getText(
                    self, #parent
                    "Input Text",   #Title
                    "Enter Your Text!",
                    # QLineEdit.PasswordEchoOnEdit, # 주석처리해도 ㄱㅊ
                    # "default text!", # 주석 ㄱㅊ
                    )
        elif tmp_str == self.l_buttons[1]:
            ret_val, is_ok = QInputDialog.getMultiLineText(
                    self,
                    "Input Multi-Line Text",
                    "Enter Your Multi-Line Text!",
                    )
        elif tmp_str == self.l_buttons[2]:
            ret_val, is_ok = QInputDialog.getInt(
                    self,
                    'Input Integer!',
                    "Enter Yout integer value!",
                    value = 0,         # 기본 text값.
                    min = 0, max = 100, # min and max
                    step = 1,
                    ok = False,  # ok 클릭시 반환여부.
                    )    
            
            if is_ok:
                print(type(ret_val), type(is_ok))
                self.ret_label.setText(f'{ret_val}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())