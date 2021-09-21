from constants import taps, n
from random import randint
from geffe import Geffe, GeffeRegister


class Generator:
    def __init__(self, length):
        self.length_of_bit_sequence = length
        self.gef = Geffe(
                    GeffeRegister(randint(1, 2**11), taps["l11"], n["l11"]),
                    GeffeRegister(randint(1, 2**9), taps["l9"], n["l9"]),
                    GeffeRegister(randint(1, 2**10), taps["l10"], n["l10"]),
                )
        
    def geffe(self):
        return bin(self.gef.generate_bits(self.length_of_bit_sequence))
    


if __name__ == "__main__":  
    gen = Generator(10**3)
    print(gen.geffe())
