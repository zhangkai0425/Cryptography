# -*- coding: utf-8 -*-
# copy from https://www.cnblogs.com/shangwei/p/14895216.html
import base64
import logging

from Crypto.Cipher import AES


class AESCipher:
    """
    AES 工具类
    """
    def __init__(self, key, iv):
        # 只截取16位
        self.key = key[:16]
        # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求
        self.iv = iv[:16]

    def __pad(self, text):
        """
        填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充
        """
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):
        """
        加密
        """
        raw = self.__pad(raw)
        print(raw)
        # 可以选择加密方式:这里用AES进行加密
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv) # 这个类非常好用，直接实例化之后即可加密和解密，非常好！
        # 加密之后又通过了base64进行编码，主要是为了二进制编码的方便和整齐性
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        """
        解密
        """
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv) # 类的实例化
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))

def __unpad(text):
    pad = ord(text[-1])
    return text[:-pad]


if __name__ == '__main__':
    e = AESCipher('1636191920482919', "dsllssdldsllssdl") # 实例化 AESCipher(self, key, iv)
    secret_data = "Learning Crytography is so interesting!"
    enc_str = e.encrypt(secret_data)
    print('enc_str: ' + enc_str.decode())
    dec_str = e.decrypt(enc_str)
    print('dec str: ' + dec_str)
