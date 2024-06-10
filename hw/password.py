import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class PasswordInput(QDialog):
    def __init__(self, correct_password):
        super().__init__()
        self.correct_password = correct_password
        
        self.setWindowTitle("비밀번호 입력")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        label = QLabel("비밀번호를 입력하세요: ")
        layout.addWidget(label)
        
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password) # 비밀번호 입력 시 마스킹
        self.password_edit.setMaxLength(10)
        layout.addWidget(self.password_edit)
        
        self.enter_button = QPushButton("Enter")
        self.enter_button.clicked.connect(self.check_password)
        layout.addWidget(self.enter_button)
        
        self.setLayout(layout)
        
    def check_password(self):
        password = self.password_edit.text()
        if password == self.correct_password:
            print("비밀번호가 일치합니다.")
            self.accept()  # 비밀번호가 일치하면 QDialog를 종료합니다.
        else:
            QMessageBox.warning(self, "경고", "비밀번호가 일치하지 않습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    correct_password = "password12"  # 사용자가 지정한 비밀번호
    window = PasswordInput(correct_password)
    window.show()
    sys.exit(app.exec())
        