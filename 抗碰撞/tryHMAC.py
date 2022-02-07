# -*- coding:UTF-8 -*-
import base64
import hashlib
import hmac
import time
# 利用HMAC生成抗碰撞的数字签名
def HMAC(message, key):
    message = message.encode()  # 加密内容
    key = key.encode()          # 加密的 key
    result = hmac.new(key, message, hashlib.sha1).digest()  # 返回结果：b'\xd5*\x01\xb0\xa4,y\x96\x9d`\xd7\xfcB\xe1\x95OZIe\xe7'
    _sig = base64.b64encode(result).decode()
    return _sig

# 一个不抗攻击的比较方法
def Verify_1(key,msg,sig):
    print('Verify_1:',HMAC(msg,key),sig)
    if len(sig) != len(HMAC(msg,key)):
        return False
    result = True
    for x,y in zip(HMAC(msg,key),sig):
        if x!=y:
            result = False
            return result
    return result
    
# 一个抗攻击的比较方法
def Verify_2(key,msg,sig):
    mac = HMAC(msg,key)
    return HMAC(key,mac) == HMAC(key,sig)

# 一个抗攻击的比较方法
def Verify_3(key,msg,sig):
    if len(sig) != len(HMAC(msg,key)):
        return False
    result = 0
    for x,y in zip(HMAC(msg,key),sig):
        result |= ord(x)^ord(y)
    return result == 0

if __name__ == '__main__':
    mess = "I love you"
    key = "1314"
    result_sig = HMAC(mess, key)
    result_sig_wrong = 'A' + result_sig
    print("result_sig:", result_sig)

    t1 = time.time()
    cmp = Verify_1(key,mess,result_sig)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)

    t1 = time.time()
    cmp = Verify_1(key,mess,result_sig_wrong)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)

    t1 = time.time()
    cmp = Verify_2(key,mess,result_sig)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)

    t1 = time.time()
    cmp = Verify_2(key,mess,result_sig_wrong)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)

    t1 = time.time()
    cmp = Verify_3(key,mess,result_sig)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)

    t1 = time.time()
    cmp = Verify_3(key,mess,result_sig_wrong)
    t2 = time.time()
    # 时间太短了，还看不出来明显的差别，如果用高级的攻击手段，是可以看到字符串比对时间差异的
    print("time is:",t2-t1)
    print(cmp)
    
    # 说实话，我也不知道为啥第一个逐字比较方法的速度总是最慢的