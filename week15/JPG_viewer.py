import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QListWidgetItem, QVBoxLayout, QWidget,
    QStatusBar, QPushButton, QWhatsThis
)
from PySide6.QtGui import QFont, QColor, QIcon
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QListWidget Roles Ex")
        
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.whats_this_bt = QPushButton("What's This?")
        self.whats_this_bt.clicked.connect(self.toggle_whats_this_mode)
        layout.addWidget(self.whats_this_bt)
        
        self.edit_button = QPushButton("Edit Item")
        self.edit_button.clicked.connect(self.edit_selected_item)
        layout.addWidget(self.edit_button)
        
        item1 = QListWidgetItem("Display Role Tex 1")
        item1.setData(Qt.DisplayRole, "Update Display Role Text 1")
        item1.setData(Qt.ToolTipRole, "ToolTip Role Text 1")
        item1.setData(Qt.StatusTipRole, "Status Role Text 1")
        item1.setData(Qt.WhatsThisRole, "What's This Role Text 1")
        
        font1 = QFont("Arial", 12, QFont.Bold)
        item1.setData(Qt.FontRole, font1)
        
        item1.setData(Qt.TextAlignmentRole, Qt.AlignCenter)
        
        background_color1 = QColor(Qt.red)
        item1.setData(Qt.BackgroundRole, background_color1)
        
        foreground_color1 = QColor(Qt.yellow)
        item1.setData(Qt.ForegroundRole, foreground_color1)
        
        item1.setData(Qt.CheckStateRole, Qt.Checked)
        
        icon1 = QIcon("path/to/icon1.png")  # 아이콘 파일 경로
        item1.setData(Qt.DecorationRole, icon1)

        # QListWidget에 아이템 추가
        self.list_widget.addItem(item1)

        # 두번째 QListWidgetItem 생성
        item2 = QListWidgetItem("Display Role Text 2")
        item2.setData(Qt.DisplayRole, "Updated Display Role Text 2")
        # item2.setData(Qt.EditRole, "Edit Role Text 2") # not working
        item2.setData(Qt.ToolTipRole, "ToolTip Role Text 2")
        item2.setData(Qt.StatusTipRole, "StatusTip Role Text 2")
        item2.setData(Qt.WhatsThisRole, "What's This Role Text 2")

        font2 = QFont("Times New Roman", 10)
        font2.setItalic(True)
        item2.setData(Qt.FontRole, font2)

        item2.setData(Qt.TextAlignmentRole, Qt.AlignRight)

        background_color2 = QColor(Qt.green)
        item2.setData(Qt.BackgroundRole, background_color2)

        foreground_color2 = QColor(Qt.blue)
        item2.setData(Qt.ForegroundRole, foreground_color2)

        item2.setData(Qt.CheckStateRole, Qt.Unchecked)

        icon2 = QIcon("path/to/icon2.png")  # 아이콘 파일 경로
        item2.setData(Qt.DecorationRole, icon2)

        # QListWidget에 아이템 추가
        self.list_widget.addItem(item2)

        # QListWidget에 항목 위에 마우스를 올렸을 때 StatusTipRole 데이터를 상태바에 표시
        self.list_widget.itemEntered.connect(self.show_status_tip)

        # QListWidget의 항목에 마우스를 올리기 위해 설정
        self.list_widget.setMouseTracking(True)

    def toggle_whats_this_mode(self):
        # "What's This?" 모드를 토글함
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()

    def show_status_tip(self, item):
        # 항목의 StatusTipRole 데이터를 상태바에 표시
        status_tip = item.data(Qt.StatusTipRole)
        self.status_bar.showMessage(status_tip)

    def edit_selected_item(self):
        # 선택된 항목을 편집 모드로 바꿈
        current_item = self.list_widget.currentItem()
        current_item.setFlags(current_item.flags() | Qt.ItemIsEditable)  # 편집 가능하도록 설정

        if current_item:
            self.list_widget.editItem(current_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())