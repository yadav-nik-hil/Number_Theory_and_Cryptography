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

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

def DecipherSmallPrime(ciphertext, modulo, exponent):
  if modulo % 2 == 0:
    small_prime = 2
    big_prime = modulo // 2
    return Decrypt(ciphertext, small_prime, big_prime, exponent) #This function is in the other RSA Quiz codes.
  
  for i in range(3, 1000001, 2):
    if prime[i] and modulo % i == 0:
      small_prime = i
      big_prime = modulo // i
      return Decrypt(ciphertext, small_prime, big_prime, exponent) #This function is in the other RSA Quiz codes.
  return "don't know"


prime = SieveOfEratosthenes(1000000)

ciphertext = 2275574988111277110437311214647848935000427550724521671610776681372035260669927879546598212402059626568529572296378786125308417822064565716822176055495534704248368924219660507214955218285229437531331022539446136060045737304497347919927268903882567968402406701512120140117419155759639779776379512631504909857
modulo = 4517997441484302732739462818197633745340869919448215356148620255867108411028738486895653782573554891335084161684285442351914740415677262295900238601126392055761648706990593425725625329173683080677363007706828763867611649178136159927562319810830366004181626803874119100160889961902072311468445073289996506931
exponent = 1927740953777951565602110467665746890410015037617105427402060961409149865403375973001399584612131360178672080227818127622463053259278787951537329431243
decrypt_third_puzzle = DecipherSmallPrime(ciphertext, modulo, exponent)
print(decrypt_third_puzzle)