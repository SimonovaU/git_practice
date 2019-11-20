# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

#!/usr/bin/python3



import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QGridLayout, QLabel, QLineEdit, QErrorMessage) 


class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        


    def initUI(self):
        self.label1 = QLabel("A", self)
        self.label2 = QLabel("B", self)
        
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        
        self.button = QPushButton("Рассчитать", self)        
        self.button.setToolTip('Нажмите, чтобы рассчитать сумму, разность, произведение и частное A и B')
        self.button.clicked.connect(lambda: showresult(self, self.edit1, self.edit2, self.edit3, self.edit4, self.edit5, self.edit6))
        
        
        self.label3 = QLabel("Сумма", self)
        self.label4 = QLabel("Разность", self)
        self.label5 = QLabel("Произведение", self)
        self.label6 = QLabel("Частное", self)
        
        self.edit3 = QLineEdit()
        self.edit3.setReadOnly(True)
        self.edit4 = QLineEdit()
        self.edit4.setReadOnly(True)
        self.edit5 = QLineEdit()
        self.edit5.setReadOnly(True)
        self.edit6 = QLineEdit()
        self.edit6.setReadOnly(True)
        
        grid =QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.edit1, 1, 1)
        grid.addWidget(self.edit2, 2, 1)
        grid.addWidget(self.button, 2, 2)
        grid.addWidget(self.label3, 1, 4)
        grid.addWidget(self.label5, 2, 4)
        grid.addWidget(self.edit3, 1, 5)
        grid.addWidget(self.edit4, 2, 5)
        grid.addWidget(self.label4, 1, 6)      
        grid.addWidget(self.label6, 2, 6)
        grid.addWidget(self.edit5, 1, 7)
        grid.addWidget(self.edit6, 2, 7)
        
        self.setLayout(grid)      
        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle('Calc')
        self.show()
        
        
        
        def showresult(self, edit1, edit2, edit3, edit4, edit5, edit6):
            self.i1 = int(self.edit1.text())
            self.i2 = int(self.edit2.text())
            if self.i2 == 0:
                self.error_dialog = QErrorMessage()
                self.error_dialog.showMessage('О нет! Деление на ноль!')
            else:
                self.i3 = self.i1 + self.i2
                self.i5 = self.i1 - self.i2
                self.i4 = self.i1 * self.i2
                self.i6 = self.i1 / self.i2
                self.edit3.setText(str(self.i3))
                self.edit4.setText(str(self.i4))
                self.edit5.setText(str(self.i5))
                self.edit6.setText(str(self.i6))
        
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    




