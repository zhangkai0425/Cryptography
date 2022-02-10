#### 认证加密：

认证加密(AE, Authenticated Encryption)或关联数据的认证加密(AEAD, Authenticated Encryptioni with Associated Data)是一种加密形式，它能同时保证数据的机密性(confidentiality)和完整性(integrity或authenticity)。这些属性通过一个单一的易于使用的编程接口来提供。

原理上，认证加密包括之前实现的加密算法+完整性数字签名算法(Mac)，实现中，往往两者结合实现。需要注意的是应当先对明文加密之后再加数字签名标签，以最大可能避免选择明文攻击方法的破解。

课程中学习的一些重要截图如下：

[<img src="https://s4.ax1x.com/2022/02/10/HNpDRs.jpg" alt="HNpDRs.jpg"  />](https://imgtu.com/i/HNpDRs)

[![HN9nln.jpg](https://s4.ax1x.com/2022/02/10/HN9nln.jpg)](https://imgtu.com/i/HN9nln)



[![HN9lwT.jpg](https://s4.ax1x.com/2022/02/10/HN9lwT.jpg)](https://imgtu.com/i/HN9lwT)

调库实现认证加密的代码，请运行`python AE.py`

需要提前安装 cryptography库：

`pip install cryptography`

