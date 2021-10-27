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
    print(f'HI_sqrt = {HI_sqrt}\n')

    alpha_0_01 = 0.01
    alpha_0_05 = 0.05
    alpha_0_1 = 0.1

    l = 255
    Z_qntl_0_01=sps.norm(loc=0, scale=1).ppf(1-alpha_0_01)
    HI_a_sqrt_0_01 = np.sqrt(2 * l) * Z_qntl_0_01 + l

    Z_qntl_0_05=sps.norm(loc=0, scale=1).ppf(1-alpha_0_05)
    HI_a_sqrt_0_05 = np.sqrt(2 * l) * Z_qntl_0_05 + l

    Z_qntl_0_1=sps.norm(loc=0, scale=1).ppf(1-alpha_0_1)
    HI_a_sqrt_0_1 = np.sqrt(2 * l) * Z_qntl_0_1 + l

    print(f'HI_a_sqrt_0_01 = {HI_a_sqrt_0_01}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_01:
        print("True")
    else:
        print("False")
    
    print(f'HI_a_sqrt_0_05 = {HI_a_sqrt_0_05}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_05:
        print("True")
    else:
        print("False")
    
    print(f'HI_a_sqrt_0_1 = {HI_a_sqrt_0_1}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_1:
        print("True")
    else:
        print("False")

def Test_2(file_name):
    file = open(file_name, 'r')
    s = file.readlines()
    HI_sqrt = 0
    n = int(len(s) / 2) 
    pairs_arr = []
    print('Form pairs:')

    d_pair = {}
    d_first = {}
    d_second = {}

    for i in trange(n):
        x = s[2*i][:-1]
        y = s[2*i+1][:-1]

        if (x,y) not in d_pair:
            d_pair[(x,y)] = 0
        d_pair[(x,y)] += 1

        if x not in d_first:
            d_first[x] = 0
        d_first[x] += 1

        if y not in d_second:
            d_second[y] = 0
        d_second[y] += 1


        # pairs_arr.append([x,y])
    count = 0

    # first_arr = []
    # second_arr = []
    # for _ in range(256):
    #     first_arr.append(0)
    #     second_arr.append(0)

    # print('Fill first_arr:')
    # for i in trange(256):
    #     for x in pairs_arr:
    #         if x[0] == str(i):
    #             first_arr[i] += 1
    # print('Fill second_arr:')
    # for i in trange(256):
    #     for x in pairs_arr:
    #         if x[1] == str(i):
    #             second_arr[i] += 1
            


    print('Count statistic Hi_sqrt:')
    for i in trange(256):
        for j in range(256):
            v_ij = 0
            v_i = 0
            a_j = 0
            #v_ij = pairs_arr.count([str(i),str(j)])
            v_ij = d_pair.get((str(i),str(j)), 0)
            
            v_i = d_first.get(str(i), 0)
            a_j = d_second.get(str(j), 0)
            #v_i = first_arr[i]
            #a_j = second_arr[j]     
            try:
                HI_sqrt += (v_ij**2) / (v_i * a_j)
            except ZeroDivisionError:
                continue
    
    HI_sqrt = n * (HI_sqrt - 1)
    print(f'HI_sqrt = {HI_sqrt}')
    
    alpha_0_01 = 0.01
    alpha_0_05 = 0.05
    alpha_0_1 = 0.1

    l = 255**2
    Z_qntl_0_01=sps.norm(loc=0, scale=1).ppf(1-alpha_0_01)
    HI_a_sqrt_0_01 = np.sqrt(2 * l) * Z_qntl_0_01 + l

    Z_qntl_0_05=sps.norm(loc=0, scale=1).ppf(1-alpha_0_05)
    HI_a_sqrt_0_05 = np.sqrt(2 * l) * Z_qntl_0_05 + l

    Z_qntl_0_1=sps.norm(loc=0, scale=1).ppf(1-alpha_0_1)
    HI_a_sqrt_0_1 = np.sqrt(2 * l) * Z_qntl_0_1 + l

    print(f'HI_a_sqrt_0_01 = {HI_a_sqrt_0_01}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_01:
        print("True")
    else:
        print("False")
    
    print(f'HI_a_sqrt_0_05 = {HI_a_sqrt_0_05}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_05:
        print("True")
    else:
        print("False")
    
    print(f'HI_a_sqrt_0_1 = {HI_a_sqrt_0_1}', end=' =>  ')
    if HI_sqrt < HI_a_sqrt_0_1:
        print("True")
    else:
        print("False")
    
    


def main():
    file_name1 = 'BBS_byte.txt'
    file_name2 = 'BBS_bit.txt'
    file_name3 = 'BM_byte.txt'
    file_name4 = 'BM_bit.txt'
    file_name5 = 'embedded_gen.txt'
    file_name6 = 'Librarian.txt'
    file_name7 = 'geffe.txt'
    file_name8 = 'l20.txt'
    file_name9 = 'l89.txt'
    file_name10 = 'lehmerhigh.txt'
    file_name11 = 'lehmerlow.txt'
    file_name12 = 'wolfram.txt'
    print("\nTest 1:")
    print(f'{file_name1}')
    print(Test_1(file_name1))
    print(f'{file_name2}')
    print(Test_1(file_name2))
    print(f'{file_name3}')
    print(Test_1(file_name3))
    print(f'{file_name4}')
    print(Test_1(file_name4))
    print(f'{file_name5}')
    print(Test_1(file_name5))
    print(f'{file_name6}')
    print(Test_1(file_name6))
    print(f'{file_name7}')
    print(Test_1(file_name7))
    print(f'{file_name8}')
    print(Test_1(file_name8))
    print(f'{file_name9}')
    print(Test_1(file_name9))
    print(f'{file_name10}')
    print(Test_1(file_name10))
    print(f'{file_name11}')
    print(Test_1(file_name11))
    print(f'{file_name12}')
    print(Test_1(file_name12))

    print("\nTest 2:")
    print(f'{file_name1}')
    print(Test_2(file_name1))
    print(f'{file_name2}')
    print(Test_2(file_name2))
    print(f'{file_name3}')
    print(Test_2(file_name3))
    print(f'{file_name4}')
    print(Test_2(file_name4))
    print(f'{file_name5}')
    print(Test_2(file_name5))
    print(f'{file_name6}')
    print(Test_2(file_name6))
    print(f'{file_name7}')
    print(Test_2(file_name7))
    print(f'{file_name8}')
    print(Test_2(file_name8))
    print(f'{file_name9}')
    print(Test_2(file_name9))
    print(f'{file_name10}')
    print(Test_2(file_name10))
    print(f'{file_name11}')
    print(Test_2(file_name11))
    print(f'{file_name12}')
    print(Test_2(file_name12))
    


if __name__ == '__main__':
    main()