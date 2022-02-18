import random

def fastExpMod(b, e, m):
    # 快速幂算法
    """
    e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

    b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
        = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n)) 

    b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
    """
    e = int(e)
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

def primeTest(n):
    q = n - 1
    k = 0

    while q % 2 == 0:
        k += 1;
        q /= 2
    a = random.randint(2, n-2);
    #If a^q mod n= 1, n maybe is a prime number
    if fastExpMod(a, q, n) == 1:
        return "inconclusive"
    #If there exists j satisfy a ^ ((2 ^ j) * q) mod n == n-1, n maybe is a prime number
    for j in range(0, k):
        if fastExpMod(a, (2**j)*q, n) == n - 1:
            return "inconclusive"
    #a is not a prime number
    return "composite"


def extendedGCD(a, b):
    # 拓展欧几里得算法
    #a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    #a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    #a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    # 修复bug:辗转相除法有问题
    while b != 0:
        q = a // b
        #ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 - q*x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)

def selectE(fn, halfkeyLength):
    while True:
        #e and fn are relatively prime
        e = random.randint(0, 1<<halfkeyLength)
        (x, y, r) = extendedGCD(e, fn)
        if r == 1:
            return e

def computeD(fn, e):
    print(fn,e)
    (x, y, r) = extendedGCD(fn, e)
    print('debug1:',x,y,r)
    #y maybe < 0, so convert it 
    if y < 0:
        return fn + y
    return y

def keyGeneration(p,q,e):
    #generate public key and private key
    n = p * q
    fn = (p-1) * (q-1)
    d = computeD(fn, e)
    print('debug:',d)
    return (n, e, d)

def encryption(M, e, n):
    #RSA C = M^e mod n
    return fastExpMod(M, e, n)

def decryption(C, d, n):
    #RSA M = C^d mod n
    return fastExpMod(C, d, n)

if __name__ == "__main__":
    #Unit Testing
    (n, e, d) = keyGeneration(13,19,7)
    print(n,e,d)
    #AES keyLength = 256
    X = 13
    C = encryption(X, e, n)
    M = decryption(C, d, n)
    print("PlainText:", X)
    print("Encryption of plainText:", C)
    print("Decryption of cipherText:", M)
    print("The algorithm is correct:", X == M)