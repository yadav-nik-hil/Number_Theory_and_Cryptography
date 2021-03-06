# -*- coding: utf-8 -*-
"""
@author: Nikhil Yadav
"""


import sys, threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

def ConvertToInt(message_str):  # Converts message to integers 
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res
  
def PowMod(a, n, mod): # Converts message(int), exponent, public key to ciphertext 
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

def Encrypt(message, modulo, exponent):
  return PowMod(ConvertToInt(message), exponent, modulo)

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
  
modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)  #This function is in the other RSA Quiz codes.
print(ciphertext)
print(DecipherSmallPrime(ciphertext, modulo, exponent))
