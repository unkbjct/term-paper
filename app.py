import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test app with sin(x)")

        self.label = QLabel()
        self.label.setText("test label 123")

        self.canvas = MplCanvas(self)
        self.plot_graph()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)

    def plot_graph(self):
        x = np.linspace(-10, 10, 100)
        y = np.sin(x)
        self.canvas.axes.plot(x, y)
        self.canvas.axes.set_title('y = sinx(x)')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())