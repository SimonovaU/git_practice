# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:09:27 2019

@author: SimonovaUV
"""
from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def _init_(self, parent=None):
        QtWidgets.QWidget._init_(self,parent)
        self.label = QtWidgets.QLabel("Hello World!")
        self.label.setAlighment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtWidgets.QPushButton("&Close the window")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.box)
        self. connect (self.btnQuit, QtCore.SIGNAL("clicked()"),
QtWidgets.qApp.quit)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("My first object oriented programme")
    window.resize(300,70)
    window.show()
    sys.exit(app.exec_())
    

