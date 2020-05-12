# -*- coding: utf-8 -*-
"""
@author: Nikhil Yadav
"""

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]
    
def gcd(a, b):
  if b==0:
    return a
  return gcd(b,a%b)
  
def ex_gcd(a,b):
  if a==0:
    return (0,1)
  (x,y) = ex_gcd(b%a,a)
  #print('x = ',x,', y = ',y)
  #print('returns = ',y-(b//a)*x,x)
  return ((y - (b//a) *x) , x)
  
def diophantine(a, b, c):
  d = gcd(a,b)
  #print('d = ',d)
  # return (x, y) such that a * x + b * y = c
  a1 = a//d
  b1 = b//d
  c1 = c//d
  (x,y) = ex_gcd(a1,b1)
  #print('got at last ',x,y)
  return (c1*x , c1*y)


def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = diophantine(n1, n2,1)
  return ((n1*x*r2) + (n2*y*r1))%(n1*n2)

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

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # Substitute this implementation with your code from question 7 of the "RSA Quiz".
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  return ConvertToStr(IntSqrt(r))

first_ciphertext = 1695925818934701958536732606471007147871697773728881305981426383004125888187531096540654444788889942827682032651915812560
first_modulo = 2019703097262944143745237345710626601616589344196612447233041278945420303895066774752152001687355425741826173570952817341
second_ciphertext = 438180481071044087096048173519586369091293503891810459558098521655659500752405553498472135529822589328291372879622802017
second_modulo = 968914506353797853274340817936111164236562754898105214422095149641604042531040243209810736059746240506447210425767208577

decrypt_seventh_puzzle = DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo)
print(decrypt_seventh_puzzle)