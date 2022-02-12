# Merkle Puzzles 密钥交换程序，加密方式采取AES算法

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

# 加密函数
def encrypt(text,key):
    key = key.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text,key):
    key = key.encode('utf-8')
    iv = b'qqqqqqqqqqqqqqqq'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text,errors='ignore').rstrip('\0')

def to_bin(value, num):#十进制数据，二进制位宽
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串

if __name__ == '__main__':
    # Alice:
    # 16位密钥,生成2^16个puzzles,存入puzzles.txt文件中
    # puzzles格式:'Puzzle:xj+kj'
    # kj为共享密钥
    # 生成方式
    j = 97
    s = ''
    for i in range(26):
        key = to_bin(i,16)
        xj = chr(j)
        kj = chr(j)
        j = j+1
        c = 'Puzzle:%s+%s'%(xj,kj)
        # print(encrypt(c,key).decode())
        s += encrypt(c,key).decode() + '\n'
    with open('puzzles.txt','w') as f:
        f.write(s)
        f.close()

    # Bob:
    # 随机选取一个进行解密,此例中，我们就选择第7个进行解密,即puzzle.txt第七行,不想再写一遍读文件了
    # 如果解密成功,即开头是Puzzle,则我们得到的共享密钥kj应当是 kj = g
    choose_s = 'db078aaf8b53b5274b2d22b5fd039e9d'
    choose_s = choose_s.encode()
    ans = ''
    s = ''
    for i in range(26):
        key = to_bin(i,16)
        d = decrypt(choose_s,key)
        if d[0:6]=='Puzzle':
            ans = d.split('+')[-1]
            print('find the solution!')
    print('共享密钥是:',ans)

    # e = encrypt("hello world",'9999999999999999')  # 加密
    # # print(type(e))
    # # s = e.decode()
    # # print(s,s.encode())
    # s = '8572914becf187f3f9e9744fc953c6bf'
    # d = decrypt(s.encode(),'9999999999999999')  # 解密
    # print("加密:", e)
    # print("解密:", d)

    # 此方法共享密钥的双方代价为O(n)级别,攻击者(窃听)破解代价为O(n^2)级别,从而实现quadratic gap(平方鸿沟)安全