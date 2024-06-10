import sys
import traceback

PYSIDE = True
try:
    from PySide6.QtWidgets import (QApplication, QWidget,
                                   QMainWindow,
                                   QLabel,
                                   QHBoxLayout,
                                   )
    from PySide6.QtCore import Qt
except:
    e_msg = traceback.format_exc()
    print(e_msg)
    PYSIDE = False
    
class GYLabel(QLabel):
    
    def __init__(self, text, color):
        super().__init__(text)
        self.setStyleSheet(f"background-color: {color}")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        