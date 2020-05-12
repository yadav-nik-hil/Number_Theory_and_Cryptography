# -*- coding: utf-8 -*-
"""
@author: Nikhil Yadav
"""

def gcd(a, b):
  if b==0:
    return a
  return gcd(b,a%b)
  
def ex_gcd(a,b):
  if a==0:
    return (0,1)
  (x,y) = ex_gcd(b%a,a)
  return ((y - (b//a) *x) , x)
  
def diophantine(a, b, c):
  d = gcd(a,b)
  #print('d = ',d)
  # return (x, y) such that a * x + b * y = c
  a1 = a//d
  b1 = b//d
  c1 = c//d
  (x,y) = ex_gcd(a1,b1)
  return (c1*x , c1*y)
  
def divide(a, b, n):
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  (p,q) = diophantine(a,n,1)
  return b*p


