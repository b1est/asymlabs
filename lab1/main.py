from constants import count_mask, lehmer_const, taps, n
from random import randint
from geffe import Geffe, GeffeRegister, Lfsr
from lehmer import LehmerLow, LehmerHigh
from wolfram import Wolfram
from multiprocessing import Pool
import argparse

class Generator:

    def __init__(self, length):
        self.length_of_bit_sequence = length
        self.geffe_ = Geffe(
                    GeffeRegister(randint(1, count_mask(n["l11"])), taps["l11"], n["l11"]),
                    GeffeRegister(randint(1, count_mask(n["l9"])), taps["l9"], n["l9"]),
                    GeffeRegister(randint(1, count_mask(n["l10"])), taps["l10"], n["l10"]),
                )
        self.lehmer_low_ = LehmerLow(lehmer_const)
        self.lehmer_high_ = LehmerHigh(lehmer_const)
        self.l20_ = Lfsr(randint(1, count_mask(n['l20'])), taps['l20'], n['l20'])
        self.l89_ = Lfsr(randint(1, count_mask(n['l89'])), taps['l89'], n['l89'])
        self.wolfram_ = Wolfram(32)

    def geffe(self):
        geffe_ = self.geffe_.generate_bits(self.length_of_bit_sequence)
        geffe_len = len(bin(geffe_)) - 2
        print((self.length_of_bit_sequence - geffe_len)*'0'+bin(geffe_)[2:])

    def lehmer_low(self):
        lehmer_low_, first_block = self.lehmer_low_.generate_bits(self.length_of_bit_sequence)
        lehmer_low_len = len(bin(lehmer_low_))-2
        first_block_len = len(bin(first_block))-2
        if first_block_len == 8:
            if lehmer_low_len == self.length_of_bit_sequence:
                print(bin(lehmer_low_)[2:])
            else:
                lehmer_low_ >>= abs((self.length_of_bit_sequence-lehmer_low_len))
                print(bin(lehmer_low_)[2:])
        else:
            if lehmer_low_len == self.length_of_bit_sequence:
                lehmer_low_ >>= abs((8-first_block_len))
                
                lehmer_low_= '0'+bin(lehmer_low_)[2:]
                while len(lehmer_low_) != self.length_of_bit_sequence:
                    lehmer_low_ = '0' + lehmer_low_
                print( lehmer_low_)
            elif lehmer_low_len < self.length_of_bit_sequence:
                lehmer_low_= '0'+bin(lehmer_low_)[2:]
                while len(lehmer_low_) != self.length_of_bit_sequence:
                    lehmer_low_ = '0' + lehmer_low_
                print( lehmer_low_)
            else:
                lehmer_low_ >>= abs(abs(self.length_of_bit_sequence-lehmer_low_len)+8-first_block_len)
                lehmer_low_= '0' + bin(lehmer_low_)[2:]
                while len(lehmer_low_) != self.length_of_bit_sequence:
                    lehmer_low_ = '0' + lehmer_low_
                print( lehmer_low_)
        
    def lehmer_high(self):
        lehmer_high_, first_block = self.lehmer_high_.generate_bits(self.length_of_bit_sequence)
        lehmer_high_len = len(bin(lehmer_high_))-2
        first_block_len = len(bin(first_block))-2
        if first_block_len == 8:
            if lehmer_high_len == self.length_of_bit_sequence:
                print( bin(lehmer_high_)[2:])
            else:
                lehmer_high_ >>= abs((self.length_of_bit_sequence-lehmer_high_len))
                print( bin(lehmer_high_)[2:])
        else:
            if lehmer_high_len == self.length_of_bit_sequence:
                lehmer_high_ >>= abs((8-first_block_len))
                
                lehmer_high_= '0'+bin(lehmer_high_)[2:]
                while len(lehmer_high_) != self.length_of_bit_sequence:
                    lehmer_high_ = '0' + lehmer_high_
                print( lehmer_high_)
            elif lehmer_high_len < self.length_of_bit_sequence:
                lehmer_high_= '0'+bin(lehmer_high_)[2:]
                while len(lehmer_high_) != self.length_of_bit_sequence:
                    lehmer_high_ = '0' + lehmer_high_
                print( lehmer_high_)
            else:
                lehmer_high_ >>= abs(abs(self.length_of_bit_sequence-lehmer_high_len)+8-first_block_len)
                lehmer_high_= '0' + bin(lehmer_high_)[2:]
                while len(lehmer_high_) != self.length_of_bit_sequence:
                    lehmer_high_ = '0' + lehmer_high_
                print( lehmer_high_)

    def l20(self):
        l20_ = self.l20_.generate_bits(self.length_of_bit_sequence)
        l20_len = len(bin(l20_)) - 2
        print( (self.length_of_bit_sequence - l20_len)*'0'+bin(l20_)[2:])
    
    def l89(self):
        l89_ = self.l89_.generate_bits(self.length_of_bit_sequence)
        l89_len = len(bin(l89_)) - 2
        print( (self.length_of_bit_sequence - l89_len)*'0'+bin(l89_)[2:])

    def wolfram(self):
        wolfram_ = self.wolfram_.generate_bits(self.length_of_bit_sequence)
        wolfram_len = len(bin(wolfram_)) - 2
        print( (self.length_of_bit_sequence - wolfram_len)*'0'+bin(wolfram_)[2:])

def results_of_generators(generator: Generator,  processes: int):
        funcs = (generator.geffe, generator.lehmer_low, generator.lehmer_high, generator.l20, generator.l89, generator.wolfram)
        pool = Pool(processes=processes)
        sub_processes = []
    
        for func in funcs:
            r = pool.apply_async(func)
            sub_processes.append(r)
        pool.close()
        pool.join()

if __name__ == "__main__":  
    generator = Generator(10**6)
    results_of_generators(generator, 4)
    
    
    
  
    
