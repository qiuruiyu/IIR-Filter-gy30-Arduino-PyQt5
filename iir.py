import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from filter import IIR2Filter, IIRFilter
import pandas as pd
import serial


# data_csv = pd.read_csv('data.csv')
# data = data_csv.values
'''
Read data from arduino serial port 
'''
serial = serial.Serial('COM3', 9600, timeout=2)
serial.flushInput()

'''
store the x and y and filtered value f_y 
'''
x = []
y = []
f_y = []
idx = 0

'''
get the sos coefficient of iir filters 
'''
sos = signal.butter(4, 20, fs=1000, output='sos', btype='low')
# an IIR filter object 
iir2 = IIRFilter(sos)


'''
realtime data processing 
'''
plt.ion()

while True:
    x.append(idx)
    idx += 1 

    data = serial.readline().decode('gbk')
    data = float(data.replace('\r\n', ''))
    y.append(data)
    plt.subplot(2, 1, 1)
    plt.title('raw data')
    plt.plot(x, y, 'b')

    f_y.append(iir2.filter(data))
    plt.subplot(2, 1, 2)
    plt.title('filtered data')
    plt.plot(x, f_y, 'r')
    plt.draw()
    plt.pause(0.01)
