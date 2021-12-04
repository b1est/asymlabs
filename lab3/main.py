from random_prime import random_prime_number
from math import ceil, sqrt
from random import randint
from wolfram import Wolfram

def jacobi(a, n):
        assert(n > a > 0 and n%2 == 1)
        t = 1
        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t
            a, n = n, a
            if a % 4 == n % 4 == 3:
                t = -t
            a %= n
        if n == 1:
            return t
        else:
            return 0

def byte_length(i):
    return ceil(i.bit_length() / 8.0)

class user:
    def __init__(self, n):
        self.__p = random_prime_number(n)
        self.__q = random_prime_number(n)
        self.n = self.__p*self.__q
        self.b = randint(0, self.n-1)

def format(m, r, l):
    return 255*pow(2,8*(l-2))+m*pow(2, 64)+r

def encrypt(m, n, b):
    r = Wolfram(32).generate_bits(64)
    print(len(bin(r))-2)
    x = format(m, r, byte_length(n))
    
    y = (x*(x+b)) % n
    c1 = (x+b/2) % 2
    c2 = jacobi(x+b/2, n)
    return (y, c1, c2)

def main():
    
    a = user(256)
    ser_n = int(input(), 16)
    ser_b = int(input(), 16)
    print(hex(int(sqrt(ser_n))+1)[2:])
    m = int(input(), 16)
    res = encrypt(m, ser_n, ser_b)
    print(hex(res[0])[2:], res[1], res[2])

main()