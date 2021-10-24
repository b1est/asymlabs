from os import path
from tqdm import trange
import time
import scipy.stats as sps
import numpy as np
from itertools import count, product, repeat, zip_longest

from artem import BBS_byte


def Test_1(file_name):
    file = open(file_name, 'r')
    s = file.readlines()
    HI_sqrt = 0
    n = len(s) / 256
    for j in trange(256):
        v = 0
        y = str(j)
        for i in s:
            x = i[:-1] 
            if x == y:
                v += 1
        HI_sqrt += ((v - n)**2) / n
    print(HI_sqrt)

    alpha = 0.01
    l = 255
    Z_qntl=sps.norm(loc=0, scale=1).ppf(1-alpha)
    HI_a_sqrt = np.sqrt(2 * l) * Z_qntl + l

    print(HI_a_sqrt)

    if HI_sqrt < HI_a_sqrt:
        return True
    return False

def Test_2(file_name):
    file = open(file_name, 'r')
    s = file.readlines()
    HI_sqrt = 0
    n = int(len(s) / 2) 
    pairs_arr = []
    print('Form pairs:')
    for i in trange(n):
        x = s[2*i][:-1]
        y = s[2*i+1][:-1]
        pairs_arr.append([x,y])
    count = 0

    first_arr = []
    second_arr = []
    for _ in range(256):
        first_arr.append(0)
        second_arr.append(0)

    print('Fill first_arr:')
    for i in trange(256):
        for x in pairs_arr:
            if x[0] == str(i):
                first_arr[i] += 1
    print('Fill second_arr:')
    for i in trange(256):
        for x in pairs_arr:
            if x[1] == str(i):
                second_arr[i] += 1
            


    print('Count statistic Hi_sqrt:')
    for i in trange(256):
        for j in range(256):
            v_ij = 0
            v_i = 0
            a_j = 0
            v_ij = pairs_arr.count([str(i),str(j)])
            
            v_i = first_arr[i]
            a_j = second_arr[j]        
            try:
                HI_sqrt += (v_ij**2) / (v_i * a_j)
            except ZeroDivisionError:
                continue

    HI_sqrt = n * (HI_sqrt - 1)
    print(f'HI_sqrt = {HI_sqrt}')
    
    alpha = 0.01
    l = 255**2
    Z_qntl=sps.norm(loc=0, scale=1).ppf(1-alpha)
    HI_a_sqrt = np.sqrt(2 * l) * Z_qntl + l
    print(f'HI_a_sqrt = {HI_a_sqrt}')

    if HI_sqrt < HI_a_sqrt:
        return True
    return False


def main():
    file_name1 = 'BBS_byte.txt'
    file_name2 = 'BBS_bit.txt'
    file_name3 = 'BM_byte.txt'
    file_name4 = 'BM_bit.txt'
    file_name5 = 'embedded_gen.txt'
    file_name6 = 'Librarian.txt'
    # print(Test_1(file_name1))
    # print(Test_1(file_name2))
    # print(Test_1(file_name3))
    # print(Test_1(file_name4))
    # print(Test_1(file_name5))
    # print(Test_1(file_name6))

    # print(Test_2(file_name1))
    # print(Test_2(file_name2))
    # print(Test_2(file_name3))
    # print(Test_2(file_name4))
    # print(Test_2(file_name5))
    print(Test_2(file_name6))

if __name__ == '__main__':
    main()