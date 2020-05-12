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
  low = IntSqrt(modulo) - 5000
  high = IntSqrt(modulo)+1
  for i in range(low,high+1):
    if modulo % i ==0:
      small_prime = i
      big_prime = modulo // small_prime
      return Decrypt(ciphertext, small_prime, big_prime, exponent)

    
ciphertext = 17250119573232938159495151836907345788113398812430175654066191733201327934519622049877939234487323106446778939262441322441499883118016470240906983286600405405975275723333283015774857915215814576298063848917112178624770247286048114974808099004729887688547429197942578127510912101233759373809217128865040107305284699411659572170044538767976158851028945020639377891878532187396172245359826784724912031113990729909962190626715090093246089745719249482899605241682396631713155172212615370473237731019162671529937751370463768746592055682933647328743947355593762481102849672215738899019205704001633289554719966
modulo = 51719336593283668370261446912126485319255258778617224708410520647959236475322767644636584229070380964088870777607922268179572997129414217601241230215567764098337343256793524076040868978141016236299799031426456716364496058717536559180352016088612210860181989844954906788705998058534134464446292058222426189127398972577715363401457729737792004774929189832678271680193791993183578966529414824171500027009334274604018078392873654591487139190491950796770048687394408709037045383279375259210879772320878973829171531428762995383292175994184457145115155299673171196041635346062296031613203020122378411630001719
exponent = 2370692877507893030572035746060036014373915956107619689350920177346027898716147057536168003507966056257828756067470679338655825857154534154205294932307
decrypt_fourth_puzzle = DecipherSmallDiff(ciphertext, modulo, exponent)
print(decrypt_fourth_puzzle)