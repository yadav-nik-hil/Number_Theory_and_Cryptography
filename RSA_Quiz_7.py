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
  # Fix this implementation
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  return ConvertToStr(IntSqrt(r))
  

p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
ciphertext1 = Encrypt("attack", n1, 2)
ciphertext2 = Encrypt("attack", n2, 2)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
print(message)