import sys # python process와 상호작용 module

from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QProgressBar,
                               QPushButton,
                               QWidget, QVBoxLayout)

from PySide6.QtCore import QTimer # QtCOre: 그려지지 않는 위젯들
                                # QTimer : 어떤 시간 간격을 기준으로 signal을 보냄(정해진 시간 끝나면 timeout signal발생-> 그 때 event 발생 가능)
class MW(QMainWindow):
    
    def __init__(self):  # instance method
        super(MW, self).__init__() # MW를 상속받고 초기화함 
        self.setWindowTitle("ex: QProgressBar")
        self.setGeometry(200,200,300,150) 
        
        self.progressBar = QProgressBar(self, minimum=9, maximum=20)
        self.progressValue = self.progressBar.minimum()
        #self.progressBar.setGeometry(50,50,200,30) # absolute positioning으로 position 설정
        
        self.startButton = QPushButton("start", self)
        #self.startButton.setGeometry(100,100,100,30)
        self.startButton.clicked.connect(self.startProgress)

        self.timer = QTimer(self) # self -> instance attribute로 유지됨 / self x -> local scope: 해당 method 동작 끝나면 사라짐
        self.timer.timeout.connect(self.updateProgress)

        lm = QVBoxLayout()
        lm.addWidget(self.progressBar)
        lm.addWidget(self.startButton)

        tmp = QWidget() # 만들고나서 접근할 일 x -> self x
        tmp.setLayout(lm)

        self.setCentralWidget(tmp)
        self.show()

    def startProgress(self):
        self.progressBar.reset()
        self.progressValue = self.progressBar.value() # Camel naming에 의해
        #self.progressValue = 0 
        self.startButton.setEnabled(False)
        self.progressBar.setValue(self.progressValue)
        self.timer.start(100)  # 100 milliseconds마다 타이머 발생 / stop 시키기 전까진 계속 time out event발생

    def updateProgress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= self.progressBar.maximum():
            self.timer.stop()
            # self.progressBar.reset() # reset시켜서 다시 반복될 수 있도록 함
            self.startButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
    