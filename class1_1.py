import os
if __name__ == '__main__':
    with open('明文.txt') as f:
        txt = f.read()
        f.close()
    # txt 为明文内容
    txt = txt.lower()
    # key 为密钥内容
    key = [(ord(i)-ord('a')) for i in 'password']
    key_l = len(key)
    # n 为计算循环加密中间变量
    n = [0]*len(txt)
    for i in range(len(txt)):
        if ord(txt[i]) > ord('z') or ord(txt[i]) < ord('a'):
            n[i] = txt[i]
            continue
        n[i] = chr((ord(txt[i]) - ord('a') + key[i%key_l])%26 + ord('a'))
    s = ''.join(n)
    print(s)
    with open('密文.txt','w') as f:
        f.write(s)
        f.close()