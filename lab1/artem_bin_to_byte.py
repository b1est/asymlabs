file = open('embedded_gen.txt','r')
s = file.read()
file.close()
file = open('embedded_gen.txt','w')
tmp_str = ''
k = 0
while len(s) != 0:
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

file3 = open('Librarian.txt','r')
s = file3.read()
file3.close()
file3 = open('Librarian.txt','w')
tmp_str = ''
k = 0
while len(s) != 0:
    print(len(s))
    if len(s) > 8:
        tmp_str = s[:8]
        tmp_str = str(int(tmp_str, 2))
        file3.write(f'{tmp_str}\n')
        k += 1
        s = s[8:]
    else:
        tmp_str = '0'*(8-len(s))
        tmp_str += s
        file3.write(f'{tmp_str}\n')
        s = ''
file3.close()