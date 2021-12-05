from random import randint
from helper import hard_mod, iverson_symbol, removePadding, sqrt

class Rabin:
    @staticmethod
    def encrypt(x, b, n):
        y = (x*(x+b)) % n
        b = hard_mod(b, n)
        parity = ((x + b) % n) % 2
        jacobi = iverson_symbol(x+b, n)
        return y, parity, jacobi
    @staticmethod
    def decrypt(ycc, pq, b):
        n = pq[0]*pq[1]
        b = hard_mod(b, n)
        sqr = (ycc[0]+pow(b, 2))
        ans = [i-b for i in sqrt(sqr, pq)]
        for x in ans:
            c1 = ((x+b) % n) % 2
            c2 = iverson_symbol(x+b, n)
            if c1 == ycc[1] and c2 == ycc[2]:
                return x
        return 0

    @staticmethod
    def signature(x, pq):
        sign = sqrt(x, pq)
        return sign[randint(0, 3)]

    @staticmethod
    def verify(m, sign, n):
        x1 = pow(sign, 2, n)
        x2 = removePadding(hex(x1)[2:])
        if m == hex(x2)[2:].upper():
            return True
        return False
