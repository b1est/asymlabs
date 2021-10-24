import numpy as np
import random
from typing import TextIO
from warnings import simplefilter
from tqdm import trange
import math
import gmpy2 as gm
import sys
from io import StringIO
import os
def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def embedded_gen(n):
    with open("embedded_gen.txt", "w") as f:
        f.write("".join(map(str,  np.random.randint(0,2,size=n) ) ) )
    # print(*np.random.randint(0,2,size=n), sep="")



def BM_bit(n):
    p = 'CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3'
    a = '5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356'
    
    file = open('BM_bit.txt', 'w')

    p_int = int(p,16)
    a_int = int(a,16)
    T_curr = random.randint(0,p_int)
    file.write(f'{str(int(T_curr < (p_int - 1) / 2))}')
    for i in trange(n - 1):
        T_next = gm.powmod(a_int, T_curr, p_int)
        file.write(f'{str(int(T_next < (p_int - 1) / 2))}')
        T_curr = T_next
    print()
    file.close()
        

def BM_byte(n):
    p = 'CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3'
    a = '5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356'
    
    p_int = int(p,16)
    a_int = int(a,16)

    file = open('BM_byte.txt', 'w')

    T_curr = random.randint(0,p_int)
    tmp = (256 * T_curr) / (p_int - 1) 
    file.write(f'{str(math.floor(tmp))}\n')
    for i in trange(n - 1):
        T_next = gm.powmod(a_int, T_curr, p_int)
        tmp = (256 * T_next) / (p_int - 1)
        if isinstance(tmp, int):
            x = str(math.floor(tmp) - 1)
            x = x[0:-2]
            file.write(f'{x}\n')
        else:
            x = str(math.floor(tmp))
            x = x[0:-2]
            file.write(f'{x}\n')
        T_curr = T_next
    print()
    file.close()


def BBS_bit(m):
    p = 'D5BBB96D30086EC484EBA3D7F9CAEB07'
    q = '425D2B9BFDB25B9CF6C416CC6E37B59C1F'
    
    p_int = int(p,16)
    q_int = int(q,16)
    
    n = p_int * q_int
    
    file = open('BBS_bit.txt', 'w')

    r_prev = random.randint(0, 1000)
    for i in trange(m):
        r_curr = gm.powmod(r_prev, 2, n)
        file.write(f'{r_curr % 2}')
        r_prev = r_curr
    print()
    file.close()


def BBS_byte(m):
    p = 'D5BBB96D30086EC484EBA3D7F9CAEB07'
    q = '425D2B9BFDB25B9CF6C416CC6E37B59C1F'
    
    p_int = int(p,16)
    q_int = int(q,16)
    
    n = p_int * q_int   

    file = open('BBS_byte.txt', 'w')

    r_prev = random.randint(0, 1000)
    for i in trange(m):
        r_curr = gm.powmod(r_prev, 2, n)
        file.write(f'{r_curr % 256}\n')
        r_prev = r_curr
    print()
    file.close()


def Librarian(n): # n - Dlina fragmenta
    with open("new_text.txt", 'r') as text:
        str_text = text.read()
        s_arr = bytearray(str_text, "utf-8")
        bin_lst = []

        file = open('Librarian.txt', 'w')
        
        r = random.randint(0, len(str_text) - n)
        print(f"Text : \n{s_arr[r:r+n]} \n Len = {len(s_arr[r:r+n])}")
        for byte in s_arr[r:r+n]:
            binary_rep = bin(byte)
            binary_rep = binary_rep[2:]
            while len(binary_rep) < 8:
                binary_rep = f"0{binary_rep}"
            bin_lst.append(binary_rep)

        for i in trange(len(bin_lst)):
            for j in bin_lst[i]:
                file.write(f'{j}')
        print()
        file.close()


# def Librarian(n): # n - Dlina fragmenta
#     import hashlib
    
#     with open("new_text.txt", 'r') as text:
#         str_text = text.read()

#         file = open('Librarian.txt', 'w')
        
#         r = random.randint(0, len(str_text) - n - 1000)

#         for i in range(n):
#             temp_string = str_text[r+i:r+i+999]
#             m = hashlib.sha256()
#             m.update(temp_string.encode())
#             answer = int(m.hexdigest(), 16)

#             file.write("0" if answer %2==0 else "1")    
#         print()
#         file.close()

def main():
    n = 10_000
    # n = int(input("Input length of seq:"))
    print(f'\n{embedded_gen.__name__}:')
    # enter = input('Enter ....')
    embedded_gen(n)
    print(f'\n{BM_bit.__name__}:')
    # enter = input('Enter ....')
    BM_bit(n)
    print(f'\n{BM_byte.__name__}:')
    # enter = input('Enter ....')
    BM_byte(n)
    print(f'\n{BBS_bit.__name__}:')
    # enter = input('Enter ....')
    BBS_bit(n)
    print(f'\n{BBS_byte.__name__}:')
    # enter = input('Enter ....')
    BBS_byte(n)
    print(f'\n{Librarian.__name__}:')
    # enter = input('Enter ....')
    Librarian(n)

    
    


if __name__ == '__main__':
    main()