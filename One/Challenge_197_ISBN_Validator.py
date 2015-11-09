"""
Challenge #197 [Easy] ISBN Validator

ISBN's (International Standard Book Numbers) are identifiers for books.
Given the correct sequence of digits, one book can be identified out of millions of others thanks to this ISBN.
But when is an ISBN not just a random slurry of digits? That's for you to find out.

For example :
0-7475-3269-9 is Valid because
(10 * 0) + (9 * 7) + (8 * 4) + (7 * 7) + (6 * 5) + (5 * 3) + (4 * 2) + (3 * 6) + (2 * 9) + (1 * 9) = 242
which can be divided by 11 and have no remainder
"""

def isbn(a):
    #string --> bool
    suma = 0
    i = 10

    for number in a:
        if number.isdigit():
            suma += int(number) * i
            i -= 1
        elif number == 'X':
            suma += 10

    if suma % 11 == 0:
        return True
    else:
        return False

a1 = '0-7475-3269-9'
a = '156881111X'
b = '123459876'
c = '1111111111'
d = '7788990000'

print isbn(c)