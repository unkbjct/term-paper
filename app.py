import sys
import core
import numpy as np

import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QGridLayout, QHBoxLayout, QLineEdit, QPushButton, QFormLayout
from PyQt5.QtGui import QIntValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class Form(QVBoxLayout):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        layout = QFormLayout()

        self.function = QVBoxLayout()
        self.function.label = QLabel('Введите правую часть функции:')
        self.function.inpLayout = QHBoxLayout()
        self.function.inpLayout.label = QLabel("y' = ")
        self.function.inpLayout.le = QLineEdit()
        self.function.inpLayout.addWidget(self.function.inpLayout.label)
        self.function.inpLayout.addWidget(self.function.inpLayout.le)
        self.function.addWidget(self.function.label)
        self.function.addLayout(self.function.inpLayout)


        tmpWidget = QWidget()
        tmpWidget.setLayout(self.function)        
        layout.addWidget(tmpWidget)
        
        self.segments = QVBoxLayout()
        self.segments.label = QLabel('Введите отрезок [a; b]: ')
        self.segments.inpLayout = QHBoxLayout()
        self.segments.inpLayout.leA = QLineEdit()
        self.segments.inpLayout.leA.setPlaceholderText('a')
        self.segments.inpLayout.leA.setValidator(QIntValidator())
        self.segments.inpLayout.leB = QLineEdit()
        self.segments.inpLayout.leB.setPlaceholderText('b')
        self.segments.inpLayout.leB.setValidator(QIntValidator())
        self.segments.inpLayout.addWidget(self.segments.inpLayout.leA)
        self.segments.inpLayout.addWidget(self.segments.inpLayout.leB)
        self.segments.addWidget(self.segments.label)
        self.segments.addLayout(self.segments.inpLayout)

        tmpWidget = QWidget()
        tmpWidget.setLayout(self.segments)
        layout.addWidget(tmpWidget)

        self.parts = QFormLayout()
        self.parts.label = QLabel('Введите количество участков: ')
        self.parts.le = QLineEdit()
        self.parts.le.setValidator(QIntValidator())
        self.parts.addWidget(self.parts.label)
        self.parts.addWidget(self.parts.le)
        
        tmpWidget = QWidget()
        tmpWidget.setLayout(self.parts)
        layout.addWidget(tmpWidget)

        self.y0 = QFormLayout()
        self.y0.label = QLabel('Введите значение функции в точке f(a):')
        self.y0.le = QLineEdit()
        self.y0.le.setValidator(QIntValidator())
        self.y0.addWidget(self.y0.label)
        self.y0.addWidget(self.y0.le)

        tmpWidget = QWidget()
        tmpWidget.setLayout(self.y0)
        layout.addWidget(tmpWidget)

        self.pb = QPushButton()
        self.pb.setObjectName("calculate")
        self.pb.setText("Вычислить") 
        
        layout.addWidget(self.pb)

        self.addLayout(layout)
        self.pb.clicked.connect(self.calculate)

    def calculate(self):
        formula = self.function.inpLayout.le.text()
        a = self.segments.inpLayout.leA.text()
        b = self.segments.inpLayout.leB.text()
        n = self.parts.le.text()
        y0 = self.y0.le.text()
        
        x, y = core.euler(formula, float(a), float(b), float(n), float(y0))
        
        plt.figure(figsize=(10, 10))
        plt.plot(x, y, label=r'точки Эйлера', color='b')
        plt.plot(x, y, 'o', color='r')

        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("График метода Эйлера задачи Коши")
        plt.grid(True)

        plt.show()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test app with sin(x)")

        main_layout = QVBoxLayout()
        
        form = Form()
        main_layout.addLayout(form)

        container = QWidget()
        container.setLayout(main_layout)

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