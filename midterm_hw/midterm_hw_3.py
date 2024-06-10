import sys
import random
import psutil
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

from PySide6.QtCore import QTimer

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use('QtAgg')

matplotlib.use('QtAgg')


class MyCanvas(FigureCanvas):

    def __init__(self, parent=None, figsize=(5, 5), dpi=100):

        self.fig, self.axes = plt.subplots(
            1, 2,
            figsize=figsize,
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)


class MW(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('CPU and RAM usage')

        self.plt_canvas = MyCanvas(self, (5, 10), 100)

        n_data = 10
        interval_ms = 1000  # 1초마다 업데이트
        self.x_data0 = list(range(n_data))
        self.x_data1 = list(range(n_data))
        self.y_data0 = [0] * n_data
        self.y_data1 = [0] * n_data

        self.update_plot0()
        self.old_plot_ref = None
        self.update_plot1()

        self.setCentralWidget(self.plt_canvas)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(interval_ms)  # milliseconds
        self.timer.timeout.connect(self.update_plots)
        self.timer.start()
        
    def update_plot0(self): 
        pass
    
    def update_plot1(self):  
        pass

    def update_plots(self):
        cpu_percent = psutil.cpu_percent()
        ram_percent = psutil.virtual_memory().percent

        self.y_data0 = [*self.y_data0[1:], cpu_percent]
        self.y_data1 = [*self.y_data1[1:], ram_percent]

        if self.old_plot_ref is not None:
            self.old_plot_ref.set_ydata(self.y_data1)
        else:
            self.old_plot_ref = self.plt_canvas.axes[1].plot(
                self.x_data1, self.y_data1,
                label='RAM Usage',
            )[0]
            self.plt_canvas.axes[1].grid()
            self.plt_canvas.axes[1].legend(loc='upper right')

        self.plt_canvas.axes[0].cla()
        self.plt_canvas.axes[0].plot(self.x_data0, self.y_data0, label='CPU Usage')
        self.plt_canvas.axes[0].grid()
        self.plt_canvas.axes[0].legend(loc='upper right')

        self.plt_canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())