import os, sys

from PySide6.QtWidgets import(
    QApplication, QMainWindow
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MW(QMainWindow):
    def __init__(self, ui_fstr):
        super().__init__()
        self.wnd = self.ds_get_wnd_from_ui(ui_fstr)
        self.ds_setup()
        self.setCentralWidget(self.wnd)
        self.show()
        
    def ds_setup(self):
        self.wnd.lineEdit.returnPressed.connect(self.ds_update_label)
        
    def ds_update_label(self):
        self.wnd.label.setText(f'Hello, {self.wnd.lineEdit.text()}')
        
    def ds_get_wnd_from_ui(self, ui_fstr):
        ui_loader = QUiLoader()
        root_dir = os.path.dirname(__file__)
        ui_path = os.path.join(root_dir, ui_fstr)
        
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        wnd = ui_loader.load(ui_file, None)
        ui_file.close()
        
        return wnd
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwd = MW('Ex1_QtDesigner.ui')
    sys.exit(app.exec())