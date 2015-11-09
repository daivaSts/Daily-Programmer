"""
[2014-11-19] Challenge #189 [Intermediate] Roman Numeral Conversion
The challenge, is to create a program that will allow you to convert decimal (base-10)
numbers to roman numerals as well as roman numerals to decimal numbers. The history of
roman numerals is a bit debated because of their varied use throughout history and a seeming
lack of a standard definition.
I can only be subtracted from V or X
X can only be subtracted from L or C
C can only be subtracted from D or M
Only one smaller value can be subtracted from a following larger value. (e.g. 'IIX' would be an
invalid way to represent the number 8)
IV = 4
XXXIV = 34
CCLXVII = 267
DCCLXIV = 764
CMLXXXVII = 987
MCMLXXXIII = 1983
MMXIV = 2014
MMMM = 4000
MMMMCMXCIX = 4999
"""
import math

v='IVXLCDM'

dikt = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}

def roman_to_dec(roman):
    result =  0
    while len(roman) > 1:
        if v.index(roman[0])< v.index(roman[1]):
            result += dikt[roman[1]]-dikt[roman[0]]
            roman = roman[2:]
        else:
            result += dikt[roman[0]]
            roman = roman[1:]

    if len(roman)==1:
        result  += dikt[roman[0]]
    return result


string = 'MMMMCMXCIX'
print roman_to_dec(string)


n = 4999
a4 = n%10000
a3 = n%1000
a2 = n%100
a1 = n%10

thousands = math.floor(a4/1000)
hundreds = math.floor(a3/100)
tens = math.floor(a2/10)
ones = math.floor(a1/1)



dikt = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}



def decimal_to_roman(dec):
   v='IVXLCDM'
   result =  0

   a4 = dec%10000
   a3 = dec%1000
   a2 = dec%100
   a1 = dec%10

   thousands = int(math.floor(a4/1000))
   result = thousands*'M'
   hundreds = int(math.floor(a3/100))
   tens = int(math.floor(a2/10))
   ones = int(math.floor(a1/1))

   print thousands, hundreds, tens, ones
   lst = [hundreds,tens,ones]
   k = len(str(dec))+1
   for i in lst:

       if i == 0:
           continue
       elif i < 4:
           result += v[k]*i
           print '*',result,k
       elif i == 4:
           result += v[k:k+2]
           print '**',result,k
       elif i >= 5 and i < 9:
           result += v[k+1]+v[k]*(i-5)
           print '***',result,k
       else:
           result += v[k]+v[k+2]
           print '****',result,k
       k -= 2

   return result

print decimal_to_roman(2014)



