from random import randint
class user:
    def __init__(self, pr, pb):
        self.n = pb[0]
        self.e = pb[1]
        self.d = pr


    







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