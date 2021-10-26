file = open('embedded_gen.txt','r')
s = file.read()
file.close()
file = open('embedded_gen.txt','w')
tmp_str = ''
k = 0
while len(s) != 0:
    if len(s) % 10000 == 0:
        print(len(s))
    if len(s) > 8:
        tmp_str = s[:8]
        tmp_str = str(int(tmp_str, 2))
        file.write(f'{tmp_str}\n')
        k += 1
        s = s[8:]
    else:
        tmp_str = '0'*(8-len(s))
        tmp_str += s
        file.write(f'{tmp_str}\n')
        s = ''
file.close()

file1 = open('BBS_bit.txt','r')
s = file1.read()
file1.close()
file1 = open('BBS_bit.txt','w')
tmp_str = ''
k = 0
while len(s) != 0:
    print(len(s))
    if len(s) > 8:
        tmp_str = s[:8]
        tmp_str = str(int(tmp_str, 2))
        file1.write(f'{tmp_str}\n')
        k += 1
        s = s[8:]
    else:
        tmp_str = '0'*(8-len(s))
        tmp_str += s
        file1.write(f'{tmp_str}\n')
        s = ''
file1.close()

file2 = open('BM_bit.txt','r')
s = file2.read()
file2.close()
file2 = open('BM_bit.txt','w')
tmp_str = ''
k = 0
while len(s) != 0:
    if len(s) % 10000 == 0:
        print(len(s))
    if len(s) > 8:
        tmp_str = s[:8]
        tmp_str = str(int(tmp_str, 2))
        file2.write(f'{tmp_str}\n')
        k += 1
        s = s[8:]
    else:
        tmp_str = '0'*(8-len(s))
        tmp_str += s
        file2.write(f'{tmp_str}\n')
        s = ''
file2.close()

# file4 = open('geffe.txt','r')
# s = file4.read()
# file4.close()
# file4 = open('geffe_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file4.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file4.write(f'{tmp_str}\n')
#         s = ''
# file4.close()

# file5 = open('l20.txt','r')
# s = file5.read()
# file5.close()
# file5 = open('l20_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file5.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file5.write(f'{tmp_str}\n')
#         s = ''
# file5.close()


# file6 = open('l89.txt','r')
# s = file6.read()
# file6.close()
# file6 = open('l89_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file6.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file6.write(f'{tmp_str}\n')
#         s = ''
# file6.close()

# file7 = open('lehmerhigh.txt','r')
# s = file7.read()
# file7.close()
# file7 = open('lehmerhigh_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file7.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file7.write(f'{tmp_str}\n')
#         s = ''
# file7.close()

# file8 = open('lehmerlow.txt','r')
# s = file8.read()
# file8.close()
# file8 = open('lehmerlow_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file8.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file8.write(f'{tmp_str}\n')
#         s = ''
# file8.close()

# file9 = open('wolfram.txt','r')
# s = file9.read()
# file9.close()
# file9 = open('wolfram_bytes.txt','w')
# tmp_str = ''
# k = 0
# while len(s) != 0:
#     print(len(s))
#     if len(s) > 8:
#         tmp_str = s[:8]
#         tmp_str = str(int(tmp_str, 2))
#         file9.write(f'{tmp_str}\n')
#         k += 1
#         s = s[8:]
#     else:
#         tmp_str = '0'*(8-len(s))
#         tmp_str += s
#         file9.write(f'{tmp_str}\n')
#         s = ''
# file9.close()