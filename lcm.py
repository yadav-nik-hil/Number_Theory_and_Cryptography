"""
@author: Nikhil Yadav
"""

def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
def lcm(a, b):
  assert a > 0 and b > 0
  return a*b/gcd(a,b)