from rabin import Rabin
from helper import format, message_checking, random_blum_prime_number, removePadding
from random import randint
from server import rabinServer, znpServer
from math import sqrt

class user:
    def __init__(self, n):
        self.pq = random_blum_prime_number(n//2), random_blum_prime_number(n//2)
        self.n = self.pq[0]*self.pq[1]
        self.b = randint(0, self.n-1)
        
def SerEncIDec(a, server, m):

    if isinstance(m, int):
         m = hex(m)[2:].upper()
    ycc = server.encryptServer(a.n, a.b, m)
    message = removePadding(hex(Rabin.decrypt(ycc, a.pq, a.b))[2:])
    if hex(message)[2:].upper() == m:
        return True
    return False

def IEncSerDec(a, server, m):
    
 
    xm = format(m, a.pq)
    x, m = xm[0], hex(xm[1])[2:].upper()
    y, parity, jacobi = Rabin.encrypt(x, server.b, server.modulus)
  
    message = server.decryptServer(y, parity, jacobi)
    
    if message == m:
        return True
    return False


def SerSignIVer(a, server, m, newM = ''.upper()):
    if isinstance(m, int):
        m = hex(m)[2:].upper()
    if isinstance(newM, int):
        newM = hex(newM)[2:].upper()
   
    signature = server.signServer(m)

    if newM == '':
        newM = m
    else:
        newM = newM.upper()
    if Rabin.verify(newM, int(signature, 16), server.modulus) == True:
        print('\033[32mVerification: True\033[0m')
    else:
        print('\033[31mVerification: False\033[0m')

def ISignSerVer(a, server, m, newM = ''.upper()):
    if isinstance(m, int):
        m = hex(m)[2:].upper()
    if isinstance(newM, int):
        newM = hex(newM)[2:].upper()
    if newM == '':
        newM = m
    else:
        newM = newM.upper()
    
    xm = format(int(m, 16), a.pq)
     
    x, m = xm[0], hex(xm[1])[2:].upper()
    sign = Rabin.signature(x, a.pq)
    
    if server.verifyServer(newM, sign, a.n) == True:
        print('\033[32mVerification: True\033[0m')
    else:
        print('\033[31mVerification: False\033[0m')
    
def main(size = 256):
    
    
        ser = rabinServer(size)
        print(f'Server n = {hex(ser.modulus)[2:].upper()}\nServer b = {hex(ser.b)[2:].upper()}')
        a = user(size)
        print(f'n = {hex(a.n)[2:].upper()}\nb = {hex(a.b)[2:].upper()}') 

        print("\033[36mServer encrypts, we decrypt\033[0m")
        m = message_checking(int(input('Message: '), 16), ser.modulus)
        print(f'm = {hex(m)[2:].upper()}') 
        if SerEncIDec(a, ser, m) == True:
            print("\033[32mOk!\033[0m")
        else:
            print('\033[3;31mError: Server encrypts, we decrypt\033[0m')

        print("\033[36mWe encrypt, server decrypts\033[0m")
        m = message_checking(int(input('Message: '), 16), ser.modulus)
        print(f'm = {hex(m)[2:].upper()}') 
        if IEncSerDec(a, ser, m) == True:
            print("\033[32mOk!\033[0m")
        else:
            print('\033[3;31mError: We encrypt, server decrypts\033[0m')

        print("\033[36mServer sign, we verify\033[0m")
        m = input('Message: ').upper()
        newM = input('New Message (not necessary): ').upper()
        print(f'm = {m}') 
        SerSignIVer(a, ser, m, newM)

        print("\033[36mWe sign, server verify\033[0m")
        m = input('Message: ').upper()
        newM = input('New Message (not necessary): ').upper()
        print(f'm = {m}') 
        ISignSerVer(a, ser, m, newM)

        print("\033[36mZero Knowledge Protocol\033[0m")
        a = znpServer()
    
    
        
    

main()
    





    
    






    


