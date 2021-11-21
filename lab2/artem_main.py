
class user:
    def __init__(self, pr, pb):
        self.n = pb[0]
        self.e = pb[1]
        self.d = pr


    

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


def GenerateKeyPair(p,q):
    n = p * q 
    fi_n = (p-1) * (q-1)
    e = 2**16 + 1
    d = modinv(e,fi_n)
    if (e*d) % fi_n == 1:
        print(True)
    else:
        exit(-1)
    public_key = (n,e)
    privat_key = (d)
    return privat_key, public_key 


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
    if M == pow(S,e,n):
        return True
    return False





def main():
    pA = 94334636873267704384893617784981802364847462230353795353220040769093621008911
    qA = 55124499161074487896949085671993246188616610581357385119908550606912958912259

    pB = 0
    qB = 0
# Generating keys:
    privat_keyA, public_keyA = GenerateKeyPair(pA,qA)
    privat_keyB, public_keyB = GenerateKeyPair(pA,qA)
# Creating A & B:
    A = user(privat_keyA, public_keyA)
    B = user(privat_keyB, public_keyB)
# Message:
    M = int(input('M: '))
# Encrypting message:
    C = Encrypt(M, public_keyA[1],public_keyA[0])
# Decrypting:
    M_decr = Decrypt(C, privat_keyA, public_keyA[0])
# Check if decrypted correctly:
    if M == M_decr:
        print(True)

# Forming Digital Sign:
    DS_A = Sign(M, privat_keyA, public_keyA[0])
    print(DS_A)
# Verifying if DS is correct:
    print(Verify(DS_A, public_keyA[1], public_keyA[0]))
    


    




if __name__ == "__main__":
    main()