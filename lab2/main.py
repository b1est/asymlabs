from random import randint
class MillerRabin:
    def __call__(self, p, k):
        iter = 0
        s = num_of_power(p-1)
        d = (p-1)//2**s
        x = randint(2, p-1)
        if gcd(x, p) > 1:
            print(f'{p} - складене число')
            return 1
        else:
            pass
        


def num_of_power(n, power = 2):
    if isinstance(power, int):
        s = 0
        while n % power == 0:
            s+=1
            n//=power
        return s

def gcd(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a

if __name__ == "__main__":
    MR = MillerRabin()(221, 0)
    
