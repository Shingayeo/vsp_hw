import subprocess, sys

from PySide6.QtWidgets import(
    QMainWindow, QWidget,
    QVBoxLayout,
    QLineEdit, QLabel, QPushButton,
    QApplication
)

class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
                            #class method
        lm = QVBoxLayout()  #layoutmanager #lm은 내가 text를 친다거나 뭐 이런 건드는게 없기에 걍 local 변수로
        
        self.le = QLineEdit()  #layoutedit 
        lm.addWidget(self.le)
        self.le.returnPressed.connect(self.ds_slot)
        
        self.btn = QPushButton('Run')
        lm.addWidget(self.btn)
        self.btn.clicked.connect(self.ds_slot)
        
        self.dpl = QLabel('')
        lm.addWidget(self.dpl)
        
        dummy_container = QWidget()
        dummy_container.setLayout(lm)
        
        self.setCentralWidget(dummy_container)
        self.show()
    
    def ds_slot(self):
        cmd_str = self.le.text()
        cmd = cmd_str.split()
        ret_str = self.ds_run(cmd)
        self.dpl.setText(ret_str)
        
    
    def ds_run(self, cmd, enc='cp949'):
        ret_p = subprocess.run(cmd, shell=True, capture_output=True, encoding=enc)
        return ret_p.stdout

if __name__ =="__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
        
        