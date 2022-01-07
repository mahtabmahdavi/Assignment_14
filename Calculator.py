from math import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from functools import partial


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.ui.btn_0.clicked.connect(partial(self.show_numbers, '0'))
        self.ui.btn_1.clicked.connect(partial(self.show_numbers, '1'))
        self.ui.btn_2.clicked.connect(partial(self.show_numbers, '2'))
        self.ui.btn_3.clicked.connect(partial(self.show_numbers, '3'))
        self.ui.btn_4.clicked.connect(partial(self.show_numbers, '4'))
        self.ui.btn_5.clicked.connect(partial(self.show_numbers, '5'))
        self.ui.btn_6.clicked.connect(partial(self.show_numbers, '6'))
        self.ui.btn_7.clicked.connect(partial(self.show_numbers, '7'))
        self.ui.btn_8.clicked.connect(partial(self.show_numbers, '8'))
        self.ui.btn_9.clicked.connect(partial(self.show_numbers, '9'))
        self.ui.btn_dot.clicked.connect(partial(self.show_numbers, '.'))

        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)

        self.ui.btn_sin.clicked.connect(partial(self.show_symbol, 'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.show_symbol, 'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.show_symbol, 'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.show_symbol, 'cot'))
        self.ui.btn_log.clicked.connect(partial(self.show_symbol, 'log'))
        self.ui.btn_sqrt.clicked.connect(partial(self.show_symbol, '√'))
        self.ui.btn_percent.clicked.connect(partial(self.show_symbol, '%'))
        self.ui.btn_negative.clicked.connect(partial(self.show_symbol, '-'))

        self.ui.btn_ac.clicked.connect(self.reset)
        self.ui.btn_equal.clicked.connect(self.equal)


    def show_numbers(self, number):
        self.ui.text_box.setText(self.ui.text_box.text() + number)


    def show_symbol(self, symbol):
        self.mode = symbol
        self.num1 = float(self.ui.text_box.text())
        self.ui.text_box.setText(symbol)

        
    def add(self):
        self.mode = 'add'
        self.num1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")


    def sub(self):
        self.mode = 'sub'
        self.num1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")


    def mul(self):
        self.mode = 'mul'
        self.num1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")


    def div(self):
        self.mode = 'div'
        self.num1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")


    def equal(self):
        if self.mode == 'add':
            self.num2 = float(self.ui.text_box.text())
            result = self.num1 + self.num2

        elif self.mode == 'sub':
            self.num2 = float(self.ui.text_box.text())
            result = self.num1 - self.num2

        elif self.mode == 'mul':
            self.num2 = float(self.ui.text_box.text())
            result = self.num1 * self.num2

        elif self.mode == 'div':
            self.num2 = float(self.ui.text_box.text())
            result = self.num1 / self.num2

        elif self.mode == 'sin':
            result = sin(radians(self.num1))

        elif self.mode == 'cos':
            result = cos(radians(self.num1))

        elif self.mode == 'tan':
            result = tan(radians(self.num1))

        elif self.mode == 'cot':
            result = 1 / tan(radians(self.num1))

        elif self.mode == 'log':
            result = log10(self.num1)

        elif self.mode == '√':
            result = sqrt(self.num1)

        elif self.mode == '%':
            result = self.num1 * 0.01

        elif self.mode == '-':
            result = -1 * (self.num1)
        
        self.ui.text_box.setText(str(result))


    def reset(self):
        self.ui.text_box.setText("")



if __name__ == "__main__":
    my_app = QApplication()
    main_window = Calculator()
    my_app.exec()