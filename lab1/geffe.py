from constants import count_mask
class GeffeRegister:

    def __init__(self, register, taps, size):
        self.register = register
        self.taps = taps
        self.size = size


class Geffe:
    def __init__(self, l1, l2, l3):
        self.reg1 = Lfsr(l1.register, l1.taps, l1.size)
        self.reg2 = Lfsr(l2.register, l2.taps, l2.size)
        self.reg3 = Lfsr(l3.register, l3.taps, l3.size)
        self.x = None
        self.y = None
        self.z = None
        self.s = None

    def get_bit(self):
        self.x = self.reg1.get_bit()
        self.y = self.reg2.get_bit()
        self.s = self.reg3.get_bit()
        self.z = (self.s * self.x) ^ ((1 ^ self.s) * self.y)

        return self.z

    def generate_bits(self, size):
        result = 0
        for i in range(size):
            result = (self.get_bit() << i) + result
        return result


class Lfsr:
    def __init__(self, register_init, taps, register_size, mask=None):
        self.register = register_init
        self.taps = taps
        self.register_size = register_size
        if mask:
            self.mask = mask
        else:
            self.mask = count_mask(register_size)

    def get_bit(self):
        xor = 0
        for t in self.taps:
            xor ^= (self.register >> t) & 1
        result = self.register & 1
        self.register = (xor << self.register_size - 1) | (
            (self.register >> 1) & self.mask
        )
        return result

    def generate_bits(self, size):
        result = 0
        for i in range(size):
            result = (self.get_bit() << i) + result
        return result