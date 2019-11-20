import sys
import base64
sys.path.append('function/encrypt')
from function.encrypt.Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


BS = AES.block_size
pad = lambda s: s + str((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
unpad = lambda s: s[0:-ord(s[-1])]


# 加密函数
def encrypt(text, key, iv):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    cryptos = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cryptos.encrypt(pad(text))
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text, key, iv):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt((a2b_hex(text)))
    return unpad(bytes.decode(plain_text))