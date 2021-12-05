
import re
import requests
from math import sqrt, gcd
from random import getrandbits





class rabinServer:
    def __init__(self, size):
        self.s =  requests.Session()
        url = f"http://asymcryptwebservice.appspot.com/rabin/serverKey?keySize={size}"
        r = self.s.get(url)
        self.b, self.modulus = int(r.json()['b'], 16), int(r.json()['modulus'], 16)

    def encryptServer(self, n, b, m):
        if isinstance(n, int):
            n = hex(n)[2:].upper()
        if isinstance(b, int):
            b = hex(b)[2:].upper()
        if isinstance(m, int):
            m = hex(m)[2:].upper()
        url = f"http://asymcryptwebservice.appspot.com/rabin/encrypt?modulus={n}&b={b}&message={m}"
        r = self.s.get(url).json()
        return int(r['cipherText'], 16), r['parity'], r['jacobiSymbol']

    def decryptServer(self, y, parity, jacobi):
        if isinstance(y, int):
            y = hex(y)[2:].upper()
        url = f"http://asymcryptwebservice.appspot.com/rabin/decrypt?cipherText={y}&expectedType=BYTES&parity={parity}&jacobiSymbol={jacobi}"
        
        r = self.s.get(url)
        return r.json()['message']


    def signServer(self, m):
        if isinstance(m, int):
            m = hex(m)[2:].upper()
        url = f"http://asymcryptwebservice.appspot.com/rabin/sign?message={m}"
        r = self.s.get(url).json()['signature']
        return r
    
    def verifyServer(self, m, s, n):
        if isinstance(n, int):
            n = hex(n)[2:].upper()
        if isinstance(s, int):
            s = hex(s)[2:].upper()
        if isinstance(m, int):
            m = hex(m)[2:].upper()
        url = f"http://asymcryptwebservice.appspot.com/rabin/verify?message={m}&type=BYTES&signature={s}&modulus={n}"
        r = self.s.get(url).json()['verified']
        return r



class znpServer:
    def __init__(self):
            print('Attack: ')
            self.s =  requests.Session()
            url = "http://asymcryptwebservice.appspot.com/znp/serverKey"
            n = self.s.get(url).json()['modulus']
            count = 0
            while True:
                count +=1
                t = getrandbits(2048)
                y = pow(t, 2, int(n, 16))
                zHex = self.znpChallenge(hex(y)[2:])
                z = int(zHex, 16)
                if z != t and z != -t:
                    p = gcd(z + t,int(n, 16))
                    q = int(n, 16) // p
                    if p == 1 or q == 1:
                         continue
                    print("Server N : ")
                    print(n)
                    print("Server P : ")
                    print(hex(p)[2:].upper())
                    print("Server Q : ")
                    print(hex(q)[2:].upper())
                    print("P * Q : ")
                    print(hex(p*q)[2:].upper())
                    break
            print("Attempts : ")
            print(count)
        
    def znpChallenge(self, y): 
        url = f"http://asymcryptwebservice.appspot.com/znp/challenge?y={y}"
        return self.s.get(url).json()['root']

        




