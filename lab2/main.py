from random_prime import random_prime_number, MillerRabin

class user:
    def __init__(self, size = 256):
        print('Generating p & q:')
        self.p = random_prime_number(size)
        self.q = random_prime_number(size)
        print(f'p = {hex(self.p)[2:].upper()}, q = {hex(self.q)[2:].upper()}')
        print('Generating keys:')
        self.__private_key, self.public_key = user.GenerateKeyPair(self.p, self.q)
        self.n = self.public_key[0]
        self.e = self.public_key[1]

    @staticmethod
    def GenerateKeyPair(p,q):
        n = p * q 
        fi_n = (p-1) * (q-1)
        e = 2**16 + 1
        d = user.modinv(e,fi_n)
        if (e*d) % fi_n == 1:
            print(True)
        else:
            exit(-1)
        public_key = (n,e)
        privat_key = (d)
        return privat_key, public_key 
        
    @staticmethod
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = user.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    @staticmethod
    def modinv(a, m):
        g, x, y = user.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def encrypt(self, M, e, n):
        C = pow(M, e, n)
        return C

    def decrypt(self, C):
        M = pow(C, self.__private_key, self.n)
        return M

    def sign(self, M):
        S = pow(M, self.__private_key, self.n)
        DS = (M, S)
        return DS

    def verify(self, DS, e, n):
        M = DS[0]
        S = DS[1]
        if M == pow(S, e, n):
            return True
        return False



def main():
    B = user(256)
    print(f'B.n = {hex(B.n)[2:].upper()}\nB.e = {hex(B.e)[2:].upper()}')
    ser_n = int(input('Server\'s Modulus: '), 16)
    ser_e = int(input('Server\'s Public exponent: '), 16)
    
    
    M = int(input('M: '))
    
    C = B.encrypt(M, ser_e, ser_n)
    print(f'C = {hex(C)[2:].upper()}')
    C = int(input(), 16)
    M_decr = B.decrypt(C)
    print(hex(M_decr)[2:].upper())


    


    




if __name__ == "__main__":
    main()