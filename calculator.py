# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

#!/usr/bin/python3


import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QGridLayout, QLabel, QLineEdit) 


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        label1 = QLabel("A", self)
        label2 = QLabel("B", self)
        
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        
        button = QPushButton("&Рассчитать", self)        
        button.setToolTip('Нажмите, чтобы рассчитать сумму, разность, произведение и частное A и B')
        
        label3 = QLabel("Сумма", self)
        label4 = QLabel("Разность", self)
        label5 = QLabel("Произведение", self)
        label6 = QLabel("Частное", self)
        
        edit3 = QLineEdit()
        edit4 = QLineEdit()
        edit5 = QLineEdit()
        edit6 = QLineEdit()
        
        grid =QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(label1, 1, 0)
        grid.addWidget(label2, 2, 0)
        grid.addWidget(edit1, 1, 1)
        grid.addWidget(edit2, 2, 1)
        grid.addWidget(button, 2, 2)
        grid.addWidget(label3, 1, 4)
        grid.addWidget(label5, 2, 4)
        grid.addWidget(edit3, 1, 5)
        grid.addWidget(edit4, 2, 5)
        grid.addWidget(label4, 1, 6)      
        grid.addWidget(label6, 2, 6)
        grid.addWidget(edit5, 1, 7)
        grid.addWidget(edit6, 2, 7)
        
        self.setLayout(grid)

        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle('Calc')
        self.show()
        
        
        # def calculations(self):
        #     i1, РассчитатьPressed = QLineEdit.getInt(self, "calc","A", 0, -100, 100, 1)
        #     i2, РассчитатьPressed = QLineEdit.getInt(self, "calc","B", 0, -100, 100, 1)
        #     if РассчитатьPressed:
        #         i3 = i1 + i2
        #         i4 = i1 - i2
        #         i5 = i1 * i2
        #         i6 = i1 / i2
                


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())