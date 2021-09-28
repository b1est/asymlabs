import numpy as np
import random
from typing import TextIO
from warnings import simplefilter
from tqdm import trange
import math
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
    print(*np.random.randint(0,2,size=n), sep="")



def BM_bit(n):
    p = 'CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3'
    a = '5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356'
    
    p_int = int(p,16)
    a_int = int(a,16)
    # n = 100_000 # the number of generated bits
    T_curr = random.randint(0,p_int)
    # print(T_curr)
    print(int(T_curr < (p_int - 1) / 2), end="")
    for i in trange(n - 1):
        T_next = pow(a_int, T_curr, p_int)
        print(int(T_next < (p_int - 1) / 2), end="")
        T_curr = T_next
    print()
        

def BM_byte(n):
    p = 'CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3'
    a = '5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356'
    
    p_int = int(p,16)
    a_int = int(a,16)

    T_curr = random.randint(0,p_int)
    tmp = (256 * T_curr) / (p_int - 1) 
    print(math.floor(tmp),end=", ")
    for i in trange(n - 1):
        T_next = pow(a_int, T_curr, p_int)
        tmp = (256 * T_next) / (p_int - 1)
        if isinstance(tmp, int):
            pass
            print(math.floor(tmp) - 1, end=", ")
        else:
            pass
            print(math.floor(tmp), end=", ")
        T_curr = T_next
    print()


def BBS_bit(m):
    # bin(int('D5BBB96D30086EC484EBA3D7F9CAEB07',16))
    p = 'D5BBB96D30086EC484EBA3D7F9CAEB07'
    q = '425D2B9BFDB25B9CF6C416CC6E37B59C1F'
    
    p_int = int(p,16)
    q_int = int(q,16)
    
    n = p_int * q_int

    # m = 100_000 # the number of generated bits
   

    r_prev = random.randint(0, 1000)
    for i in trange(m):
        r_curr = pow(r_prev, 2, n)
        print(r_curr % 2, end="")
        r_prev = r_curr
    print()


def BBS_byte(m):
    print(f'\n{"/"*10}\n{BBS_byte.__name__}:\n')
    p = 'D5BBB96D30086EC484EBA3D7F9CAEB07'
    q = '425D2B9BFDB25B9CF6C416CC6E37B59C1F'
    
    p_int = int(p,16)
    q_int = int(q,16)
    
    n = p_int * q_int   

    r_prev = random.randint(0, 1000)
    for i in trange(m):
        r_curr = pow(r_prev, 2, n)
        print(r_curr % 256, end=", ")
        r_prev = r_curr
    print()

def Librarian(n): # n - Dlina fragmenta

    # with open('text.txt', 'r') as f: # "Грязный" файл
    #     print(f'{f.name} is opend')

    #     s = f.read()
    #     # s = s.replace('ё','е')
    #     with open("new_text.txt", "a") as f_new: # "Чистый" файл
    #         print(f'{f_new.name} is opend')
    #         # Чистим файл от ненужных символов:
    #         for i in s:
    #             if i.isalpha():
    #                 f_new.write(i)
            # s = f_new.read()
    with open("new_text.txt", 'r') as text:
        str_text = text.read()
        s_arr = bytearray(str_text, "utf-8")
        bin_lst = []

        r = random.randint(0, len(str_text) - n)
        print(f"Text : \n{s_arr[r:r+n]} \n Len = {len(s_arr[r:r+n])}")
        for byte in s_arr[r:r+n]:
            binary_rep = bin(byte)
            binary_rep = binary_rep[2:]
            while len(binary_rep) < 8:
                binary_rep = f"0{binary_rep}"
            bin_lst.append(binary_rep)

        for i in bin_lst:
            for j in i:
                print(j, end="")
        print()

def main():
    n = int(input("Input length of seq:"))
    print(f'\n{embedded_gen.__name__}:')
    enter = input('Enter ....')
    embedded_gen(n)
    print(f'\n{BM_bit.__name__}:')
    enter = input('Enter ....')
    BM_bit(n)
    print(f'\n{BM_byte.__name__}:')
    enter = input('Enter ....')
    BM_byte(n)
    print(f'\n{BBS_bit.__name__}:')
    enter = input('Enter ....')
    BBS_bit(n)
    print(f'\n{BBS_byte.__name__}:')
    enter = input('Enter ....')
    BBS_byte(n)
    print(f'\n{Librarian.__name__}:')
    enter = input('Enter ....')
    Librarian(n)
    


if __name__ == '__main__':
    main()