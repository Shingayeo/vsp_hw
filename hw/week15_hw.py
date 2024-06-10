import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QListWidgetItem, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QMenuBar, 
    QStatusBar, QLabel, QLineEdit, QPushButton, QToolBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# 이미지를 편집하고 표시하기 위한 캔버스 클래스 정의
class ImageViewerCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = Figure()  # 캔버스에 그림을 그리는 데 사용할 Matplotlib Figure 객체 생성
        self.axis = self.figure.add_subplot(111)  # 이미지를 표시하기 위한 서브 플롯 생성
        super().__init__(self.figure)  # 부모 클래스 생성자 호출
        self.setParent(parent)  # 부모 위젯 설정
        self.setStyleSheet("background-color: #2f2f2f;")  # 배경색 설정
        self.axis.axis('off')  # 축 숨기기
        self.figure.subplots_adjust(left=0, right=1, top=1, bottom=0)  # 서브 플롯의 여백 설정
        
        # 펜 및 지우개 활성화 여부, 그리기 정보, 이미지 경로 초기화
        self.start_point = None
        self.pen_active = False
        self.eraser_active = False
        self.drawings = []
        self.image_path = None

        # 이벤트 핸들러 연결
        self.mpl_connect('button_press_event', self.on_click)
        self.mpl_connect('motion_notify_event', self.on_motion)
        self.mpl_connect('button_release_event', self.on_release)

    # 이미지 표시 메서드
    def display_image(self, image_path):
        self.image_path = image_path
        self.axis.clear()
        image = mpimg.imread(image_path)  # 이미지 로드
        self.axis.imshow(image)  # 이미지 표시
        self.axis.axis('off')  # 축 숨기기
        self.figure.subplots_adjust(left=0, right=1, top=1, bottom=0)  # 여백 설정
        self.draw()  # 그리기

        # 그려진 도형 다시 그리기
        self.redraw_drawings()  

    # 이미지 저장 메서드
    def save_image(self, save_path):
        self.figure.savefig(save_path, bbox_inches='tight', pad_inches=0)
        self.draw()

    # 마우스 클릭 이벤트 핸들러
    def on_click(self, event):
        if event.button == 1 and event.inaxes:
            if self.pen_active:
                self.start_point = (event.xdata, event.ydata)
                self.drawings.append([self.start_point])
            elif self.eraser_active:
                self.remove_drawing(event.xdata, event.ydata)
                self.redraw()

    # 마우스 이동 이벤트 핸들러
    def on_motion(self, event):
        if self.pen_active and self.start_point and event.inaxes:
            self.drawings[-1].append((event.xdata, event.ydata))
            x_coords, y_coords = zip(*self.drawings[-1])
            self.axis.plot(x_coords, y_coords, color='red')
            self.draw()
        elif not self.pen_active and not self.eraser_active and self.start_point and event.inaxes:
            if hasattr(self, 'rect'):
                self.rect.remove()
            x0, y0 = self.start_point
            x1, y1 = event.xdata, event.ydata
            self.rect = self.axis.add_patch(
                plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor='red', linewidth=2)
            )
            self.draw()

    # 마우스 릴리스 이벤트 핸들러
    def on_release(self, event):
        if self.pen_active and event.button == 1 and self.start_point and event.inaxes:
            self.start_point = None
            self.draw()
        elif not self.pen_active and not self.eraser_active and event.button == 1 and self.start_point and event.inaxes:
            self.start_point = None
            self.draw()

    # 펜 모드
    def toggle_pen_mode(self):
        self.pen_active = not self.pen_active
        self.eraser_active = False
        self.axis.set_title('Pen Mode: ON' if self.pen_active else 'Pen Mode: OFF')
        self.draw()

    # 지우개 모드 토글 메서드
    def toggle_eraser_mode(self):
        self.eraser_active = not self.eraser_active
        self.pen_active = False
        self.axis.set_title('Eraser Mode: ON' if self.eraser_active else 'Eraser Mode: OFF')
        self.draw()

    # 그리기 삭제 메서드
    def remove_drawing(self, x, y):
        for drawing in self.drawings:
            if any((abs(dx - x) < 5 and abs(dy - y) < 5) for dx, dy in drawing):
                self.drawings.remove(drawing)
                break

    # 캔버스 다시 그리기 메서드
    def redraw(self):
        self.axis.clear()
        if self.image_path:
            self.display_image(self.image_path)
        for drawing in self.drawings:
            x_coords, y_coords = zip(*drawing)
            self.axis.plot(x_coords, y_coords, color='red')
        self.draw()

    # 이미지에 그려진 도형을 다시 그리는 메서드
    def redraw_drawings(self):
        for drawing in self.drawings:
            x_coords, y_coords = zip(*drawing)
            self.axis.plot(x_coords, y_coords, color='red')
        self.draw()

# 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PNG Viewer")

        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        right_layout = QVBoxLayout()
        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        # QListWidget 생성 및 설정
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        main_layout.addWidget(self.list_widget)
        
        # Matplotlib FigureCanvas 생성 및 설정
        self.canvas = ImageViewerCanvas(self)
        
        # NavigationToolbar 생성 및 설정.
        self.nav_toolbar = NavigationToolbar(self.canvas, self)
        
        right_layout.addWidget(self.nav_toolbar)
        right_layout.addWidget(self.canvas)
        
        # Label, LineEdit, and Button for labeling
        self.label_label = QLabel("Label:")
        self.label_edit = QLineEdit()
        self.save_button = QPushButton("Save Labeled Image")
        self.save_button.clicked.connect(self.save_labeled_image)

        right_layout.addWidget(self.label_label)
        right_layout.addWidget(self.label_edit)
        right_layout.addWidget(self.save_button)

        main_layout.addWidget(right_widget)

        # StatusBar 생성
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # 메뉴바 설정
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Select Img Dir")
        menubar.setNativeMenuBar(False)

        # 디렉토리 선택 액션 추가
        open_action = QAction("Open Directory", self)
        open_action.triggered.connect(self.open_directory)
        file_menu.addAction(open_action)

        # 툴바 설정
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        pen_action = QAction(QIcon(None), "Toggle Pen", self)
        pen_action.triggered.connect(self.canvas.toggle_pen_mode)
        self.toolbar.addAction(pen_action)
        
        eraser_action = QAction(QIcon(None), "Toggle Eraser", self)
        eraser_action.triggered.connect(self.canvas.toggle_eraser_mode)
        self.toolbar.addAction(eraser_action)
    
        self.current_directory = None
        self.current_image_index = -1
        self.png_files = []
        
        self.show()

    # 디렉토리 열기 메서드
    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.current_directory = directory
            self.list_widget.clear()
            self.png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
            for png_file in self.png_files:
                item = QListWidgetItem(png_file)
                item.setData(Qt.UserRole, os.path.join(directory, png_file))
                self.list_widget.addItem(item)
            self.current_image_index = 0
            if self.png_files:
                self.display_image()

    # 이미지 항목 클릭 시 호출되는 메서드
    def on_item_clicked(self, item):
        file_path = item.data(Qt.UserRole)
        self.current_image_index = self.png_files.index(os.path.basename(file_path))
        self.display_image()
        
    # 이미지 표시 메서드
    def display_image(self):
        if 0 <= self.current_image_index < len(self.png_files):
            file_path = os.path.join(self.current_directory, self.png_files[self.current_image_index])
            self.canvas.display_image(file_path)
            self.status_bar.showMessage(f'{file_path} ({self.current_image_index + 1}/{len(self.png_files)})')
            self.list_widget.blockSignals(True)
            self.list_widget.setCurrentRow(self.current_image_index)
            self.list_widget.blockSignals(False)

    # 라벨된 이미지 저장 메서드
    def save_labeled_image(self):
        label = self.label_edit.text()
        if self.current_image_path and label:
            self.canvas.axis.text(10, 10, label, color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.5))
            save_path = self.current_image_path.replace('.png', f'_{label}.png')
            self.canvas.save_image(save_path)
            self.status_bar.showMessage(f"Labeled image saved to {save_path}")

    # 키 이벤트 핸들러
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.current_image_index = (self.current_image_index + 1) % len(self.png_files)
            self.display_image()
        elif event.key() == Qt.Key_Left:
            self.current_image_index = (self.current_image_index - 1) % len(self.png_files)
            self.display_image()
        super().keyPressEvent(event)

# 애플리케이션 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())    