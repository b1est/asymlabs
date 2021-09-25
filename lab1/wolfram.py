from constants import count_mask
from random import randint

class Wolfram:
    
    def __init__(self, bits_size, r_init = None):
        if r_init == None:
            self.r = randint(1, count_mask(bits_size))
        else:
            self.r = r_init
        self.bits_size = bits_size
        self.mask = count_mask(bits_size)
 
    def get_bit(self):
        x = self.r % 2
        self.r = ((self.r >> (self.bits_size - 1)) | ((self.r << 1) & self.mask)) ^ (self.r | ((self.r & 1 << (self.bits_size - 1)) | (self.r >> 1)))
        return x

    def generate_bits(self, size):
        result = 0
        for i in range(size):
            result = (self.get_bit() << i) | result
        return result
