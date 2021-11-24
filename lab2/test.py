from random import choice, randint
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
        pass
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
    S = pow(k, d, n)
    k1 = pow(k, e1, n1)
    S1 = pow(S, e1, n1)
    key_pair = (k1, S1)
    return key_pair

def ReceiveKey(k1, S1, n1, d1, e, n):
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    if k == pow(S, e, n):
        return True
    return False






# M = input('M: ')
# M = int(M, 16)
# print(hex(2884713662)[2:])

def main():
    choice1 = ''
    if choice1 == '1':
    # Decryption (you):
        print("""Start:
        Server - Encrypt, you - Decrypt
        """)
        n, e, d = GenerateKeyPair(size=256)
        print(f'\nn = {hex(n)[2:]}')
        print(f'e = {hex(e)[2:]}')
        C = input('C: ')
        M_new = Decrypt(int(C, 16), d, n)
        print(f'\nM (decrypted): {hex(M_new)[2:]}')
    elif choice1 == '2':
    # Encryption (you):
        n = input('n: ')
        e = input('e: ')
        n = int(n, 16)
        e = int(e, 16)
        M = input('M: ')
        C = Encrypt(int(M, 16), e, n)
        print(f'C: {hex(C)[2:]}')


    choice2 = ''
    if choice2 == '1':
    # Sign (you):
        n, e, d = GenerateKeyPair(size=256)
        print(f'n = {hex(n)[2:]}')
        print(f'e = {hex(e)[2:]}')
        M = input('M: ')
        DS = Sign(int(M, 16), d, n)
        print(f"M = {hex(DS[0])[2:]}\n S = {hex(DS[1])[2:]}")
    elif choice2 == '2':
        n = input('n: ')
        e = input('e: ')
        n = int(n, 16)
        e = int(e, 16)
        M = input('M: ')
        S = input('S: ')
        print(Verify((int(M, 16), int(S, 16)), e, n))
    

    choice3 = ''
    if choice3 == '1':
    # Send Key (you):
        n, e, d = GenerateKeyPair(256)
        n1, e1, _ = GenerateKeyPair(256)
        while n1 < n:
            n, e, d = GenerateKeyPair(256)
            n1, e1, _ = GenerateKeyPair(256)
        print(f'n = {hex(n)[2:]}')
        print(f'n1 = {hex(n1)[2:]}')
        print(f'e = {hex(e)[2:]}')
        print(f'e1 = {hex(e1)[2:]}')

        k1, S1 = SendKey(n, d, e1, n1)
        print(f'k1: {hex(k1)[2:]}\nS1: {hex(S1)[2:]}')
        
    elif choice3 == '2':
    # Recieve Key (you):
        n, e, d = GenerateKeyPair(256)
        n1, e1, d1 = GenerateKeyPair(256)
        while n1 < n:
            n, e, d = GenerateKeyPair(256)
            n1, e1, d1 = GenerateKeyPair(256)
        print(f'n  = {hex(n)[2:]}')
        print(f'n1 = {hex(n1)[2:]}')
        print(f'e = {hex(e)[2:]}')
        print(f'e1 = {hex(e1)[2:]}')

        k1 = input('k1: ')
        S1 = input('S1: ')
        
        print(ReceiveKey(int(k1, 16), int(S1, 16), n1, d1, e, n))
# Send - Recieve Key:    
    n, e, d = GenerateKeyPair(256)
    n1, e1, d1 = GenerateKeyPair(256)
    while n1 < n:
        n, e, d = GenerateKeyPair(256)
        n1, e1, d1 = GenerateKeyPair(256)
    
    k1, S1 = SendKey(n, d, e1, n1)
    print(ReceiveKey(k1, S1, n1, d1, e, n))









    # txt = """Start:
    # 1 - You - Encrypt, server - Decrypt
    # 2 - You - Decrypt, server - Encrypt
    # > """
    # choice = input(txt)
    # # choice = '1'
    # if choice == '1':
    #     n, e, d = GenerateKeyPair(256)
    #     print(f'n = {hex(n)[2:]}\n')
    #     print(f'e = {hex(e)[2:]}\n')
    # else:
    #     n = input('n: ')
    #     e = input('e: ')
    #     n = int(n, 16)
    #     e = int(e, 16)
    # if choice == '1':
    #     C = input('C: ')
    #     C = int(C, 16)
    #     M_new = Decrypt(C, d, n)
    #     print(f'\nM (decrypted) = "{hex(M_new)[2:]}"')
    # else:
    #     M = 'A1800BCF193288FFCDAECC90F89AAE200097BAED'
    #     M = int(M, 16)
    #     C = Encrypt(M, e, n)
    #     print(f'C = {hex(C)[2:]}\n')
    
    # txt = """Start:
    # 1 - You - Sign, server - Verify
    # 2 - You - Verify, server - Sign
    # > """
    # choice = input(txt)
    # if choice == '1':
    #     M = 'A1800BCF193288FFCDAECC90F89AAE200097BAED'
    #     M = int(M, 16)
    #     DS = Sign(M, d, n)
    #     print(f'({hex(DS[0])[2:]}, {hex(DS[1])[2:]})')
    # else:
    #     n, e, d = GenerateKeyPair(256)
    #     print(f'n = {hex(n)[2:]}\n')
    #     print(f'e = {hex(e)[2:]}\n')
    #     DS = [0,0]
    #     DS[0] = int('A1800BCF193288FFCDAECC90F89AAE200097BAED', 16)
    #     DS[1] = int('65A2BBF492621C0462CD62C7A2C165B09182D927871DA1488981A9A2E8C5EC38', 16)
    #     print(Verify(DS, e, n))

    # txt = """Start:
    # 1 - You - Send Key, server - Recieve Key
    # 2 - You - Recieve Key, server - Send Key
    # > """
    # choice = input(txt)
    # if choice == '1':
    #     n, e, d = GenerateKeyPair(256)
    #     n1, e1, _ = GenerateKeyPair(256)
    #     while n1 < n:
    #         n, e, d = GenerateKeyPair(256)
    #         n1, e1, _ = GenerateKeyPair(256)
    #     print(f'n1 = {hex(n1)[2:]}\ne1 = {hex(e1)[2:]}')
    #     print()
    #     print(f'n = {hex(n)[2:]}\ne = {hex(e)[2:]}')
    #     k1, S1 = SendKey(n, d, e1, n1)
    #     print(f'K1 = {hex(k1)[2:]}\nS1 = {hex(S1)[2:]}')
    # else:
    #     n = '338366D393CC12CF0EBCF51A76A9204243E7EFA0649C0BF4A4CAE78B8F2F3F77'
    #     e = '10001'
    #     n = int(n ,16)
    #     e = int(e, 16)
    #     n1, e1, d1 = GenerateKeyPair(256)
    #     while n > n1:
    #         n, e, d = GenerateKeyPair(256)
    #         n1, e1, _ = GenerateKeyPair(256)
    #     key = input('key: ')
    #     Signature = input('sig: ')
    #     key = int(key, 16)
    #     Signature = int(Signature, 16)
    #     ReceiveKey(key, Signature, n1, d1, e, n)
    n, e, d = GenerateKeyPair(256)
    n1, e1, d1 = GenerateKeyPair(256)
    while n1 < n:
        n, e, d = GenerateKeyPair(256)
        n1, e1, d1 = GenerateKeyPair(256)
    
    k1, S1 = SendKey(n, d, e1, n1)
    ReceiveKey(k1, S1, n1, d1, e, n)





    




if __name__ == "__main__":
    main()
    
 

    
    