import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMenuBar, QFileDialog, QVBoxLayout, QWidget, QMenu, QStatusBar
from PySide6.QtCore import QFileInfo

class TextFileViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("텍스트 파일 열기")

        # 현재 열려 있는 파일 경로를 저장하기 위한 변수
        self.current_file_path = None

        # 텍스트 편집기 위젯 생성
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # 상태 표시줄 생성
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        # 메뉴 바 생성
        self.create_menu()

    def create_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = QMenu("파일", self)
        menu_bar.addMenu(file_menu)

        open_action = file_menu.addAction("열기")
        open_action.triggered.connect(self.open_file)

        save_action = file_menu.addAction("저장")
        save_action.triggered.connect(self.save_file)

        save_as_action = file_menu.addAction("다른 이름으로 저장")
        save_as_action.triggered.connect(self.save_file_as)

        exit_action = file_menu.addAction("종료")
        exit_action.triggered.connect(self.close)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", "텍스트 파일 (*.txt)")
        if file_path:
            file_info = QFileInfo(file_path)
            if file_info.suffix().lower() == "txt":
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_edit.setPlainText(content)
                    self.current_file_path = file_path
                    self.update_status_bar(content)
            else:
                self.text_edit.setPlainText("선택된 파일은 텍스트 파일이 아닙니다.")
                self.status_bar.showMessage("잘못된 파일 형식", 5000)

    def save_file(self):
        if self.current_file_path:
            self._save_to_path(self.current_file_path)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "텍스트 파일 저장", "", "텍스트 파일 (*.txt)")
        if file_path:
            self._save_to_path(file_path)

    def _save_to_path(self, file_path):
        content = self.text_edit.toPlainText()
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        self.current_file_path = file_path
        self.status_bar.showMessage(f"파일 저장됨: {file_path}", 5000)

    def update_status_bar(self, content):
        char_count = len(content)
        self.status_bar.showMessage(f"글자 수: {char_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextFileViewer()
    viewer.show()
    sys.exit(app.exec())