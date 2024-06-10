import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.fstr = os.path.dirname(
            os.path.abspath(__file__)
        )
        self.setMinimumSize(600,600)
        self.setWindowTitle("Menu bar Ex")
        self.setup_main_wnd()
        self.create_actions()
        self.create_menu()
        self.show()
    
    def create_actions(self):
        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+X")
        self.quit_act.setIcon(QIcon(f"{self.fstr}/img/exit.png"))
        self.quit_act.triggered.connect(self.close)
        
    def create_menu(self):
        mb = self.menuBar()                         # main window의 menu bar를 추상화한 instance.
        menu_item = mb.addMenu("test")    # test 라는 이름의 menu item을 추가.
        menu_item.addAction(self.quit_act) # test 메뉴아이템에 아까 만든 QAction instance추가.
        mb.setNativeMenuBar(False) # for macOS

    def setup_main_wnd(self):
        label = QLabel('test')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
