import numpy as np
from math import ceil

class Lehmer:

    def __init__(self, const):
        self.m = const[0]
        self.a = const[1]
        self.c = const[2]
        self.x = np.array([const[3]])

    def calc(self, n):
        if n % 8 == 0 and n != 8:
            while n > 0 and n != 0 and n != 8:
                self.x = np.append(self.x, [(self.a*self.x[-1]+self.c)%self.m])
                n-=8
        else:
            n = ceil(n/8)*8
            while n > 0 and n != 0 and n != 8: 
                self.x = np.append(self.x, [(self.a*self.x[-1]+self.c)%self.m])
                n-=8
        return self.x

class LehmerLow (Lehmer):

    def __init__(self, const):
        Lehmer.__init__(self, const)
        self.mask = 0xff

    def generate_bits(self, n):
        Lehmer.calc(self, n)
        res = 0
        first_len = len(bin(int(self.x[0]) & self.mask))-2
        for i in self.x:
            res = (res << 8) | (int(i) & self.mask)
        return res, first_len
        
        


        
class LehmerHigh(Lehmer):

    def __init__(self, const):
        Lehmer.__init__(self, const)
        self.mask = 0xff
        
    def generate_bits(self, n):
        Lehmer.calc(self, n)  
        res = 0
        first_len = len(bin(int(self.x[0]) & self.mask))-2
        for i in self.x:
            res = (res << 8) | (int(i) >> 24)
        return res, first_len




