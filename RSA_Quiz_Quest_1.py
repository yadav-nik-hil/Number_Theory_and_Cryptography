# -*- coding: utf-8 -*-
"""
@author: Nikhil Yadav
"""

import sys, threading


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Decrypt(ciphertext, p, q, exponent): #Our main function to decrypt the message which is known ciphertext, keys (p,q), exponent
  #Fix this code
  number = (p-1)*(q-1)
  d = InvertModulo(exponent, number)
  return ConvertToStr(PowMod(ciphertext, d, p * q )) #Int gelecek bunlar degil

p = 779849711281
q = 748173698927
e = 1018651
ciphertext = 148784435264686331994392
decrypt_first_puzzle = Decrypt(ciphertext, p, q, e)
print(decrypt_first_puzzle)