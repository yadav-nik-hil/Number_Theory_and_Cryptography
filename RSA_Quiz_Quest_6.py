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

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  # Substitute this implementation with your code from question 3 of the "RSA Quiz".
  for i in range(len(potential_messages)):
    if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
      return potential_messages[i]
  return "don't know"


ciphertext = 336184023047118677086739
modulo = 1110014195838866450995043
exponent = 767549
potential_messages = ["http://goo.gl/", "http://tinyurl.com/", "http://bit.ly/", "http://t.co/", "http://ow.ly/", "https://is.gd/", "https://buff.ly/", "http://adf.ly/", "http://bit.do/"]
decrypt_second_puzzle = DecipherSimple(ciphertext, modulo, exponent, potential_messages)
print decrypt_second_puzzle
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

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  # Substitute this implementation with your code from question 3 of the "RSA Quiz".
  for i in range(len(potential_messages)):
    if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
      return potential_messages[i]
  return "don't know"


ciphertext = 336184023047118677086739
modulo = 1110014195838866450995043
exponent = 767549
potential_messages = ["http://goo.gl/", "http://tinyurl.com/", "http://bit.ly/", "http://t.co/", "http://ow.ly/", "https://is.gd/", "https://buff.ly/", "http://adf.ly/", "http://bit.do/"]
decrypt_second_puzzle = DecipherSimple(ciphertext, modulo, exponent, potential_messages)
print decrypt_second_puzzle
