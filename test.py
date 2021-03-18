import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from filter import IIR2Filter, IIRFilter
import pandas as pd
import serial
import time 
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import os 
import sys





class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        '''
        Initialize the UI
        '''
        self.resize(1100, 520)
        
        self.graphWidget1 = pg.PlotWidget(self)
        self.graphWidget2 = pg.PlotWidget(self)

        self.graphWidget1.resize(500, 500)
        self.graphWidget1.move(10, 10)
        self.graphWidget2.resize(500, 500)
        self.graphWidget2.move(550, 10)

        # 定时器
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10) # 10ms
        self.timer.timeout.connect(self.update_plot_data)  # 每次定时器时间结束就是会执行这个函数
        self.timer.start()
        '''
        get the data from the serial  
        '''
        self.serial = serial.Serial('COM5', 9600, timeout=2)
        self.serial.flushInput()

        self.x = []
        self.y = []
        self.f_y = []
        self.idx = 0

        '''
        get the sos coefficient and create iir2 obejct 
        '''
        self.sos = signal.butter(4, 20, fs=1000, output='sos', btype='low')
        # an IIR filter object 
        self.iir2 = IIRFilter(self.sos)
        '''
        initialize the draw pen and plot the x and y 
        '''
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.graphWidget1.setTitle("Raw data", size="20pt")
        self.graphWidget2.setTitle("Filtered data", size="20pt")
        self.plot = self.graphWidget1.plot(self.x, self.y, pen=pen)
        self.plot2 = self.graphWidget2.plot(self.x, self.f_y, pen=pen)

    '''
    a function used to get the index of data and the value of data / filtered data 
    '''
    def get_data(self):
        self.x.append(self.idx)
        self.idx += 1
        data = self.serial.readline().decode('gbk')
        data = float(data.replace('\r\n', ''))
        self.y.append(data)
        self.f_y.append(self.iir2.filter(data))

    '''
    a function used to update the plot realtime 
    '''
    def update_plot_data(self):
        self.get_data()
        if len(self.x) <= 200:
            self.plot.setData(self.x, self.y)
            self.plot2. setData(self.x, self.f_y)
        else:
            self.plot.setData(self.x[-200:], self.y[-200:])
            self.plot2.setData(self.x[-200:], self.f_y[-200:])


def main():
    app = QtWidgets.QApplication(sys.argv)
    main2 = MainWindow()
    main2.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
