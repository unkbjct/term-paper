import sys
import core
import numpy as np

import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QFormLayout, QComboBox, QMessageBox, QDialog
from PyQt5.QtGui import QIntValidator, QIcon

class Helper(QVBoxLayout):
    def __init__(self, parent=None):
        super(Helper, self).__init__(parent)

        self.qdl = QDialog()
        self.qdl.setWindowTitle('HELPER')
        self.qdl.setMinimumSize(200, 50)

        layout = QVBoxLayout()
        layout.title = QLabel('Вы можете использовать следующие мат функции')
        layout.title.setStyleSheet('font-size: 16px; font-weight: 800')
        layout.addWidget(layout.title)
        layout.addWidget(QLabel('sin(x) | cos(x) | tg(x)'))
        layout.addWidget(QLabel('Корень: sqrt(x)'))
        layout.addWidget(QLabel('Возведение в степень: x ** y'))
        layout.addWidget(QLabel('Натуральный логарифм: log(x)'))

        self.qdl.setLayout(layout)
        self.qdl.exec()

class Form(QVBoxLayout):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        layout = QFormLayout()

        self.isOpenGraph = False

        self.function = QVBoxLayout()
        self.function.label = QLabel('Введите правую часть функции:')
        self.function.inpLayout = QHBoxLayout()
        self.function.inpLayout.label = QLabel("y' = ")
        self.function.inpLayout.le = QLineEdit()
        self.function.inpLayout.button = QPushButton()
        self.function.inpLayout.button.setIcon(QIcon('resources/question.png'))
        self.function.inpLayout.button.clicked.connect(self.showHelp)
        self.function.inpLayout.addWidget(self.function.inpLayout.label)
        self.function.inpLayout.addWidget(self.function.inpLayout.le)
        self.function.inpLayout.addWidget(self.function.inpLayout.button)
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

        self.method = QFormLayout()
        self.method.label = QLabel('Выберите метод вычисления ОДУ:')
        self.method.cb = QComboBox()
        self.method.cb.addItem('Метод Эйлера', 0)
        self.method.cb.addItem('Метод Хона', 1)
        self.method.cb.addItem('Улучшенный метод Эйлера', 2)
        self.method.cb.addItem('Метод Рунге Кутта', 3)
        self.method.cb.addItem('Метод Адамса', 4)
        self.method.cb.addItem('Все методы', 5)
        self.method.addWidget(self.method.label)
        self.method.addWidget(self.method.cb)

        tmpWidget = QWidget()
        tmpWidget.setLayout(self.method)
        layout.addWidget(tmpWidget)

        self.pb = QPushButton()
        self.pb.setObjectName("calculate")
        self.pb.setText("Вычислить") 
        
        layout.addWidget(self.pb)

        self.addLayout(layout)
        self.pb.clicked.connect(self.calculate)

    def showHelp(self):
        helper = Helper()

    def calculate(self):
        if self.isOpenGraph:
            self.isOpenGraph = False
            plt.close()

        formula = self.function.inpLayout.le.text()
        a = self.segments.inpLayout.leA.text()
        b = self.segments.inpLayout.leB.text()
        n = self.parts.le.text()
        y0 = self.y0.le.text()
        
        method = self.method.cb.currentData()

        try:
            a, b, n, y0 = float(a), float(b), float(n), float(y0)
            
            x, y = 0, 0

            if method == 0:
                x, y = core.euler(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Метод Эйлера', color='b')
            elif method == 1:
                x, y = core.hoyne(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Метод Хойна', color='r')
            elif method == 2:
                x, y = core.besteuler(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Улучшенный метод Ейлера', color='g')
            elif method == 3:
                x, y = core.kyt(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Рунге Кутт', color='y')
            elif method == 4:
                x, y = core.adams(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Адамс', color='purple')
            else:
                x, y = core.euler(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Метод Эйлера', color='b')
                x, y = core.hoyne(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Метод Хойна', color='r')
                x, y = core.besteuler(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Улучшенный метод Ейлера', color='g')
                x, y = core.kyt(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Рунге Кутт', color='y')
                x, y = core.adams(formula, a, b, n, y0)
                plt.plot(x, y, label=r'Адамс', color='purple')

            if n < 15:
                plt.plot(x, y, 'o', color='black')

            self.isOpenGraph = True

        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText('Введенные данные не корректны!!')
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText('Вы ввели ноль частей!!')
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"График уравнения y' = {formula}")
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())