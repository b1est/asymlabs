from constants import count_mask, lehmer_const, taps, n
from random import randint
from geffe import Geffe, GeffeRegister, Lfsr
from lehmer import LehmerLow, LehmerHigh


class Generator:
    def __init__(self, length):
        self.length_of_bit_sequence = length
        self.geffe_ = Geffe(
                    GeffeRegister(randint(1, count_mask(n["l11"])), taps["l11"], n["l11"]),
                    GeffeRegister(randint(1, count_mask(n["l9"])), taps["l9"], n["l9"]),
                    GeffeRegister(randint(1, count_mask(n["l10"])), taps["l10"], n["l10"]),
                )
        self.lehmer_low = LehmerLow(lehmer_const)
        self.lehmer_high = LehmerHigh(lehmer_const)
        self.l20 = Lfsr(randint(1, count_mask(n['l20'])), taps['l20'], n['l20'])
        self.l89 = Lfsr(randint(1, count_mask(n['l89'])), taps['l89'], n['l89'])


    def geffe(self):
        return bin(self.geffe_.generate_bits(self.length_of_bit_sequence))
    


if __name__ == "__main__":  
    gen = Generator(10**3)
    
