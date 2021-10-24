from constants import count_mask, lehmer_const, taps, n
from random import randint
from geffe import Geffe, GeffeRegister, Lfsr
from lehmer import LehmerLow, LehmerHigh
from wolfram import Wolfram
from multiprocessing import Pool
from math import pow, sqrt
from scipy.stats import norm

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
        for txt in ('geffe.txt', 'l20.txt', 'l89.txt', 'lehmerhigh.txt', 'lehmerlow.txt', 'wolfram.txt'):
            f = open(txt, 'w')
            f.close()

    def geffe(self):
        geffe_ = self.geffe_.generate_bits(self.length_of_bit_sequence)
        with open("geffe.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((geffe_>>i) & 1))
        print('Geffe done!')

    def lehmer_low(self):
        lehmer_low_ = self.lehmer_low_.generate_bits(self.length_of_bit_sequence)
        with open("lehmerlow.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((lehmer_low_>>i) & 1))
        print('LehmerLow done!')
        
    def lehmer_high(self):
        lehmer_high_ = self.lehmer_high_.generate_bits(self.length_of_bit_sequence)
        with open("lehmerhigh.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((lehmer_high_>>i) & 1))
        print('LehmerHigh done!')
 

    def l20(self):
        l20_ = self.l20_.generate_bits(self.length_of_bit_sequence)
        with open("l20.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((l20_>>i) & 1))
        print('L20 done!')
    
    def l89(self):
        l89_ = self.l89_.generate_bits(self.length_of_bit_sequence)
        with open("l89.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((l89_>>i) & 1))
        print('L89 done!')

    def wolfram(self):
        wolfram_ = self.wolfram_.generate_bits(self.length_of_bit_sequence)
        with open("wolfram.txt", "a") as f:
            for i in range(self.length_of_bit_sequence):
                f.write(str((wolfram_>>i) & 1))
        print('Wolfram done!')




def results_of_generators(generator: Generator,  processes: int):
        funcs = (generator.geffe, generator.lehmer_low, generator.lehmer_high, generator.l20, generator.l89, generator.wolfram)
        pool = Pool(processes=processes)
        sub_processes = []
        for func in funcs:
            r = pool.apply_async(func)
            sub_processes.append(r)
        pool.close()
        pool.join()


class Tests: 
    def __init__(self):
        self.txt_names = ('geffe.txt', 'l20.txt', 'l89.txt', 'lehmerhigh.txt', 'lehmerlow.txt', 'wolfram.txt')
        self.alphas = (0.01, 0.05, 0.1)
        

    def uniformityTest(self):
        f = open('geffe.txt', "r").read()
        r = 16
        m2 = len(f) // r
        n = m2*r
        hi2 = 0
        l = 255*(r-1)
        f_ = [f[x:x+m2] for x in range (0, len(f), m2)]
        for i in range(0, 256):
            vi = len([i for x in range(0, len(f), 8) if int(f[x:x+8], 2) == i])
            for j in range(r):
                vi2 = pow(len([i for x in range(0, len(f_[j]), 8) if int(f_[j][x:x+8], 2) == i]), 2)
                hi2 += (vi2 / (vi * m2))
                
        print(hi2)
        hi2 = n*(hi2 - 1)
        print(f'hi2 = {hi2}')
        for alpha in self.alphas:
            hi2teor = sqrt(2*l)*norm.ppf(1-alpha)+l    
            print(f'hi2(1-{alpha}) = {hi2teor}')
            if hi2 <= hi2teor:
                print('ok')
            else:
                print('ne ok')


        


if __name__ == "__main__":
    
    # generator = Generator(10**6)
    # results_of_generators(generator, 4)

    test = Tests()
    test.uniformityTest()
    
    
    
  
    
