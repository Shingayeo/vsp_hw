import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QPushButton
from PySide6.QtCore import Signal, Qt, QObject


class MySignal(QObject):
    my_signal = Signal()


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Enter an integer:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("click")
        self.button.clicked.connect(self.button_ck)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def button_ck(self):
        try:
            value = int(self.line_edit.text())
            self.accept()
            print("Entered integer:", value)
        except ValueError:
            print("Please enter a valid integer.")


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle("midterm hw 2")
        self.my_signal = MySignal()
        self.my_signal.my_signal.connect(self.show_dialog)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.my_signal.my_signal.emit()

    def show_dialog(self):
        dialog = MyDialog(self)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MW()
    sys.exit(app.exec())