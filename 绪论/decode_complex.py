import numpy as np
if __name__ == '__main__':
    with open('密文.txt') as f:
        txt = f.read()
        f.close()
    # txt 为密文内容
    txt = txt.lower()
    # key 为密钥内容，仅仅知道密钥为8位长度
    key_l = 8 
    key = [0]*key_l
    keywords = ['']*key_l
    table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z']
    dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,
    'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    cnt = np.zeros((8,26))
    # 每隔8个点进行扫描，计算频率，按e频率最高统计密钥
    for k in range(len(key)):
        begin = k # 以 k 为开始，逐次+8
        while begin < len(txt):
            if ord(txt[begin]) > ord('z') or ord(txt[begin]) < ord('a'):
                begin += 8
            else:
                cnt[k,dict[txt[begin]]] += 1
                begin += 8
    e = ord('e') - ord('a')
    for i in range(len(key)):
        key[i] = (np.argmax(cnt[i,:]) - e)%26
        keywords[i] = chr(key[i] + ord('a'))
    print("解密得到的密钥为：",keywords)

    # n 为计算循环解密中间变量
    n = [0]*len(txt)
    for i in range(len(txt)):
        if ord(txt[i]) > ord('z') or ord(txt[i]) < ord('a'):
            n[i] = txt[i]
            continue
        n[i] = chr((ord(txt[i]) - ord('a') - key[i%key_l])%26 + ord('a'))
    s = ''.join(n)
    with open('complex解密.txt','w') as f:
        f.write(s)
        f.close() 