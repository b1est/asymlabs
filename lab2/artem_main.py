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


def RSA(p,q):
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
    return public_key, privat_key




def main():
    p = 94334636873267704384893617784981802364847462230353795353220040769093621008911
    q = 55124499161074487896949085671993246188616610581357385119908550606912958912259
    privat_key, public_key = RSA(p,q)
    print(f'Privat key:({privat_key})\nPublic key: {public_key}')




if __name__ == "__main__":
    main()