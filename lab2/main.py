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
                print(f'{hex(p)[2:].upper()} - складене число.')
                return False
            else:

                pseudosimple = MillerRabin.strongly_pseudosimple_test(p, s, d, x)
                if pseudosimple == True:
                    iter += 1
                else:
                    print(f'{hex(p)[2:].upper()} - складене число.')
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
            print(f'{hex(p)[2:].upper()} - сильно псевдопросте за основою {hex(x)[2:].upper()}.')
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
                        print(f'{hex(p)[2:].upper()} - не сильно псевдопросте за основою {hex(x)[2:].upper()}.')
                        return False
                    if xr == p-1:
                        print(f'{hex(p)[2:].upper()} - сильно псевдопросте за основою {hex(x)[2:].upper()}.')
                        return True
                    
            print(f'{hex(p)[2:].upper()} - не сильно псевдопросте за основою {hex(x)[2:].upper()}.')
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
        print(f'Згенероване число: {hex(gen)[2:].upper()}.')
        mr =  MillerRabin()(gen, 10)         
    else:
        return gen





if __name__ == "__main__":
    """
    val = 256                                                                              ДЛЯ БУДУЩЕЙ РАБОТЫ С http://asymcryptwebservice.appspot.com/rsa
    payload = {'keySize': val}
    r = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey', params=payload)
    
    print(r.json())   
    """
    size = 256
    
    A = {'p': random_prime_number(size), 'q': random_prime_number(size)}
    B = {'p': random_prime_number(size), 'q': random_prime_number(size)}
    print(A, B)
    
 

    
    