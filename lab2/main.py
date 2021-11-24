from random_prime import random_prime_number

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

# def Encrypt(M, e, n):
#     C = pow(M,e,n)
#     return C

# def Decrypt(C, d, n):
#     M = pow(C, d, n)
#     return M

# def Sign(M, d, n):
#     S = pow(M, d, n)
#     DS = (M, S)
#     return DS

# def Verify(DS, e, n):
#     M = DS[0]
#     S = DS[1]
#     if M == pow(S,e,n):
#         return True
#     return False





def main():
    
# Creating A & B:
    A = user()
    A.n = int('9AE448568F7B2EDB621B6B6A2C174519CAE7EE1AE8751AB7413CE270E66F2613', 16)
    A.e = int( "10001", 16)
    B = user()
# Message:
    M = input('M: ')
    M = int(M, 16)
# Encrypting message:
#     C = Encrypt(M, A.e, A.n)
    C = B.encrypt(M, A.e, A.n)
    print(hex(C))
# Decrypting:
#     M_decr = Decrypt(C, A.private_key, A.n)
    M_decr = B.decrypt(C)
# # Check if decrypted correctly:
    if M == M_decr:
        print(True)

# # Forming Digital Sign:
#     DS_A = Sign(M, A.private_key, A.n)
    DS_A = A.sign(M)
    print(hex(DS_A[0])[2:], hex(DS_A[1])[2:])
# # Verifying if DS is correct:
    print(B.verify(DS_A, A.e, A.n))
#     print(Verify(DS_A, A.e, A.n))
    


    




if __name__ == "__main__":
    main()