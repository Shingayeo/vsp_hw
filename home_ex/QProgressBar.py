import sys

from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QProgressBar,
                               QPushButton,
                               QWidget, QVBoxLayout)

from PySide6.QtCore import QTimer

class MW(QMainWindow):
    
    def __init__(self):
        super(MW, self).__init__()
        self.setWindowTitle("ex: QProgressBar")
        self.setGeometry(200, 200, 300, 150)
        
# ProgressBar 생성 및 button 생성
        self.progressBar = QProgressBar(minimum=0, maximum=10)
        self.progressValue = self.progressBar.minimum()
        # self.progressValue 변수 : self.progressBar 객체의 현재 값(진행률) 추적
        
        # start button click 시 작업        
        self.startButton = QPushButton("start")
        self.startButton.clicked.connect(self.startProgress)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        
        lm = QVBoxLayout()
        lm.addWidget(self.progressBar)
        lm.addWidget(self.startButton)
        
        tmp = QWidget()
        tmp.setLayout(lm)
        
        self.setCentralWidget(tmp)
        self.show()
        

    def startProgress(self):
        self.progressBar.reset()
        self.progressValue = self.progressBar.value()
        self.startButton.setEnabled(False)
        self.timer.start(100)
        
    # ProgressBar update
    def updateProgress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= self.progressBar.maximum():
            self.timer.stop()
            self.startButton.setEnabled(True)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())