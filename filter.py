import scipy.signal 
import numpy as np 


class IIR2Filter(object):

    def __init__(self, sos):
        self.order = 2 # 2nd order filter here 
        self.b = sos[0, 0:3].squeeze()  # b_0, b_1, b_2
        self.a = sos[0, 4:6].squeeze()  # (1), a_1, a_2
        self.bf1 = 0
        self.bf2 = 0

    def filter(self, x):
        x = x - self.a[0] * self.bf1 - self.a[1] * self.bf2
        y = self.b.dot(np.array([x, self.bf1, self.bf2]))
        self.bf2, self.bf1 = self.bf1, x
        return y
            

class IIRFilter(object):

    def __init__(self, sos):
        self.num = sos.shape[0]
        self.cascade = []
        for i in range(self.num):
            s = sos[i, :].reshape(1, -1)
            print(s, s.shape)
            self.cascade.append(IIR2Filter(s))

    def filter(self, x):
        for flt in self.cascade:
            x = flt.filter(x)
        return x
                




