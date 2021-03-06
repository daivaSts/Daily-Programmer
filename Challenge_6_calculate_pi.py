"""
Challenge #6 [easy]
You're challenge for today is to create a program that can calculate pi accurately to at least 30 decimal places.
"""

#from Joe_Pineapples
from decimal import Decimal, getcontext

print('How many decimal places do you want? :')
places = input()
places = int(places)
getcontext().prec = places
m = 10

a = [0]*m
b = [0]*m
t = [0]*m
p = [0]*m


one = Decimal(1)
two = Decimal(2)
four = Decimal(4)
half = one/two


a[0] = one
b[0] = one/two**(one/two)
t[0] = one/four
p[0] = one

lastpi = 0

for n in range(m-1):
    a[n+1] = (a[n]+b[n])/two
    b[n+1] = (a[n]*b[n])**half
    t[n+1] = t[n] - p[n]*(a[n]-a[n+1])**2
    p[n+1] = two*p[n]

    pi = (a[n+1] + b[n+1])**2/four/t[n+1]
    if lastpi == pi:
        break
    lastpi = pi

print('Pi calculated in', n, 'loops, as', pi)