# IIR-Filter-gy30-Arduino-PyQt5
an simple example of IIR filter, including Arduino code for gy30 sensor and python gui receiving data from Arduino serial port.

## gy30 (folder)   
an arduino program using PIO platform on VSCode. You can also find the **main.cpp** code in **src** folder.   
gy30 light sensor write / read data via **IIC agreement**.

## filter.py (Python file)
contain an **IIR2Filter class** to complete a 2nd iir filter.   
 - it allows users to get real filtered data.  
 - Every time you put a data in it, it will return you a filtered value immediately.  

also contain an **IIRFilter class** to complete a chain filter of 2nd iir filter.    
 - it consists of several 2nd iir filter in **self.cascade**.
 - also real-time.


## iir.py (Python file)
using the filter before.   
using **scipy.signal** to get the butter of goal filters, then put it in the class we achieve before.   
get real-time data from Arduino serial port and process it, then draw a ion plot to show it. 

## test.py (Python file, including PyQt5 to complete a simple GUI)
iir.py + GUI

