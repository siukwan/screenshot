# -*- coding: utf-8 -*-
import sys
import ctypes
import os  
import pyhk
from PyQt4 import QtCore, QtGui, uic
from UIpractise import Uipractise_MainWindow
# qtCreatorFile = "practise.ui" # Enter file here.
 
# Uipractise_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
# Uipractise_MainWindow, QtBaseClass = UIpractise.Ui_MainWindow()



# 继承 QThread 类
class captureThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    def __init__(self, parent=None):
        super(captureThread, self).__init__(parent)

    def run(self):
        try:
            dll = ctypes.cdll.LoadLibrary('PrScrn.dll')
        except Exception:
            print("Dll load error!")
            return
        else:
            try:
                dll.PrScrn(0)
            except Exception:
                print("Sth wrong in capture!")
                return

def captureFunction():
    mThread = captureThread()
    mThread.start()

# 继承 QThread 类
class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    def __init__(self, parent=None):
        super(BigWorkThread, self).__init__(parent)

    # 重写 run() 函数，在里面干大事。
    def run(self):
        hot = pyhk.pyhk()
        # add hotkey
        try:
            hot.addHotkey(['Alt', 'F1'], captureFunction)
            # start looking for hotkey.
            hot.start()
        except:
            print '注册失败'

class MyApp(QtGui.QMainWindow, Uipractise_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Uipractise_MainWindow.__init__(self)
        self.setupUi(self)
        # self.bwThread = BigWorkThread()
        # self.bwThread.start()

        self.captureBTN.clicked.connect(self.capture)

    def capture(self):
        try:
            dll = ctypes.cdll.LoadLibrary('PrScrn.dll')
        except Exception:
            print("Dll load error!")
            return
        else:
            try:
                dll.PrScrn(0)
            except Exception:
                print("Sth wrong in capture!")
                return

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())