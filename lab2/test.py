from random import randint
from wolfram import Wolfram

class MillerRabin:
    def __call__(self, p, k):
        iter = 0
        s = MillerRabin.num_of_power(p-1)
        d = (p-1)//2**s
        while iter < k:
            x = randint(2, p-1)
            if MillerRabin.gcd(x, p) > 1:
                # print(f'{hex(p)[2:].upper()} - складене число.')
                return False
            else:

                pseudosimple = MillerRabin.strongly_pseudosimple_test(p, s, d, x)
                if pseudosimple == True:
                    iter += 1
                else:
                    # print(f'{hex(p)[2:].upper()} - складене число.')
                    return False
                    
                       
        return True

    @staticmethod
    def horner(x, a, m):
        y = 1
        alpha = list(str(bin(a))[2:])
        alpha.reverse()
        i = len(alpha)-1
        while i >= 0:
            y = (y**2) % m
            if alpha[i] == '1':
                y = (y*x) % m
            else:
                y = y%m
            i-=1
        return y
    
    @staticmethod
    def strongly_pseudosimple_test(p, s, d, x):
        tmp = MillerRabin.horner(x, d, p)
        if tmp == 1 or tmp == p-1:
            # print(f'{hex(p)[2:].upper()} - сильно псевдопросте за основою {hex(x)[2:].upper()}.')
            return True
        else:
            xr = None
            r = 1
            while r <= s-1:
                xr = MillerRabin.horner(x, d*2**r, p)
                if xr != 1 and xr != p-1:
                    r+=1
                else:
                    if xr == 1:
                        # print(f'{hex(p)[2:].upper()} - не сильно псевдопросте за основою {hex(x)[2:].upper()}.')
                        return False
                    if xr == p-1:
                        # print(f'{hex(p)[2:].upper()} - сильно псевдопросте за основою {hex(x)[2:].upper()}.')
                        return True
                    
            # print(f'{hex(p)[2:].upper()} - не сильно псевдопросте за основою {hex(x)[2:].upper()}.')
            return False

    @staticmethod
    def num_of_power(n, power = 2):
        if isinstance(power, int):
            s = 0
            while n % power == 0:
                s+=1
                n//=power
            return s

    @staticmethod
    def gcd(a, b): 
        while b != 0: 
            a, b = b, a % b 
        return a

def random_prime_number(n):
    mr = False
    while mr == False:
        gen = Wolfram(32).generate_bits(n)
        # print(f'Згенероване число: {hex(gen)[2:].upper()}.')
        mr =  MillerRabin()(gen, 10)         
    else:
        return gen

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def GenerateKeyPair(size=256):
    p = random_prime_number(size)
    q = random_prime_number(size)
    n = p * q 
    fi_n = (p-1) * (q-1)
    e = 2**16 + 1
    d = modinv(e,fi_n)
    if (e*d) % fi_n == 1:
        print(True)
    else:
        exit(-1)
    return n, e, d 


def Encrypt(M, e, n):
    C = pow(M,e,n)
    return C

def Decrypt(C, d, n):
    M = pow(C, d, n)
    return M

def Sign(M, d, n):
    S = pow(M, d, n)
    DS = (M, S)
    return DS

def Verify(DS, e, n):
    M = DS[0]
    S = DS[1]
    if M == pow(S, e, n):
        return True
    return False

def SendKey(n, d, e1, n1):
    k = randint(1, n-1)
    k1 = pow(k, e1, n1)
    S = pow(k, d, n)
    S1 = pow(S, e1, n1)
    key_pair = (k1, S1)
    return key_pair

def ReceiveKey(k1, S1, n1, d1, e, n):
    k = pow(k1, d1, n1)
    S = pow(S1, d1)
    if k == pow(S, e, n):
        return True
    return False






# M = input('M: ')
# M = int(M, 16)
# print(hex(2884713662)[2:])

def main():
    n, e, d = GenerateKeyPair(1024)
    M = input('M: ')
    M = int(M, 16)
    C = Encrypt(M, e, n)
    M_new = Decrypt(C, d, n)
    print(hex(M_new)[2:])

    




if __name__ == "__main__":
    main()
    
 

    
    