# -*- coding: utf-8 -*-
"""
@author: Nikhil Yadav
"""


import sys, threading
import math

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

def Encrypt(message, modulo, exponent):
  return PowMod(ConvertToInt(message), exponent, modulo)
  
def Decrypt(ciphertext, p, q, exponent): #Our main function to decrypt the message which is known ciphertext, keys (p,q), exponent
  #Fix this code
  number = (p-1)*(q-1)
  d = InvertModulo(exponent, number)
  return ConvertToStr(PowMod(ciphertext, d, p * q )) #Int gelecek bunlar degil

def DecipherSmallPrime(ciphertext, modulo, exponent):
  
  if modulo % 2 == 0:
    small_prime = 2
    big_prime = modulo // 2
    return Decrypt(ciphertext, small_prime, big_prime, exponent) #This function is in the other RSA Quiz codes.
  
  for i in range(3, 1000000, 2):
    if modulo % i == 0:
      small_prime = i
      big_prime = modulo // i
      return Decrypt(ciphertext, small_prime, big_prime, exponent) #This function is in the other RSA Quiz codes.
  return "don't know"

def IntSqrt(x):
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

def DecipherSmallDiff(ciphertext, modulo, exponent):
  low = IntSqrt(n) - 5000
  high = IntSqrt(n)+1
  for i in range(low,high+1):
    if modulo % i == 0:
      small_prime = i
      big_prime = modulo // small_prime
      return Decrypt(ciphertext, small_prime, big_prime, exponent)
  
p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)
