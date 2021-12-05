from random import getrandbits, randint
from wolfram import Wolfram
from sympy.ntheory import jacobi_symbol
import math

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
                       #  print(f'{hex(p)[2:].upper()} - сильно псевдопросте за основою {hex(x)[2:].upper()}.')
                        return True
                    
           #  print(f'{hex(p)[2:].upper()} - не сильно псевдопросте за основою {hex(x)[2:].upper()}.')
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
        #print(f'Згенероване число: {hex(gen)[2:].upper()}.')
        
        mr =  MillerRabin()(gen, 10)
                     
    else:
        #print(f'{gen} - просте.')
        return gen


def random_blum_prime_number(n):
    mr = False
    while mr == False:
        gen = Wolfram(32).generate_bits(n)
        #print(f'Згенероване число: {hex(gen)[2:].upper()}.')
        if gen % 4 != 3:
            continue
        mr =  MillerRabin()(gen, 10)
                     
    else:
        #print(f'{gen} - просте.')
        return gen

def hard_mod( b, n):
    if b % 2 == 0:
        return (b//2) % n
    else: 
        return ((b + n) // 2) % n

def jacobi(a, n):
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    if n % 2 == 0:
        raise ValueError("'n' must be odd.")
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0

def iverson_symbol(a, b):
    j = jacobi_symbol(a, b)
    if j == 1:
        return 1
    else:
        return 0

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def byte_length(i):
    return math.ceil(i.bit_length() / 8.0)

def format(m,  pq):
    l = byte_length(pq[0]*pq[1])
    x = 0
    while jacobi_symbol(x, pq[0]) != 1 or jacobi_symbol(x, pq[1]) != 1:
        r = getrandbits(64)
        x = 255*pow(2,8*(l-2))+m*pow(2, 64)+r
    return x, m

def mulinv(b, n):
    res = gcdExtended(b, n)
    g = res[0]
    x = res[1]
    if g == 1:
        return x%n
    return 0

def sqrt(y, pq):
    n = pq[0]*pq[1]
    s1 = pow(y, (pq[0]+1)//4, pq[0])
    s2 = pow(y, (pq[1]+1)//4, pq[1])
    u = mulinv(pq[0], pq[1])
    v = (1 - u * pq[0]) // pq[1]

    a = u * pq[0] * s2
    c = v * pq[1] * s1
    x1 = (a + c) % n
    x2 = (a - c) % n
    x3 = (c - a) % n
    x4 = (0 - a - c) % n
    return [x1, x2, x3, x4]


def removePadding(mHex):
    m = int(mHex,16)
    bytess = []
    while (m // 256 != 0):
        bytess.append((m % 256))
        m //= 256
    
    bytess.append(m)
    m = 0
    for i in range(8, len(bytess)-1):
        j = i - 8
        m += bytess[i]*256**j
    return m


def message_checking(m, n):
    l_n = byte_length(n)
    l_m = byte_length(m)
    try:
       
        assert m > int(math.sqrt(n))
        assert l_m <= l_n - 10
    except:
        m = int(input(f'Please enter message grater than {hex(int(math.sqrt(n)))[2:].upper()} and length must not exceed {l_n-10} bytes: '), 16)
        m = message_checking(m, n)
    return m