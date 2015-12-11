# -*- coding: utf-8 -*-
'''
[4/12/2012] Challenge #39 [easy]
You are to write a function that displays the numbers from 1 to an input parameter n, one per line, except that if
the current number is divisible by 3 the function should write “Fizz” instead of the number, if the current number
is divisible by 5 the function should write “Buzz” instead of the number, and if the current number is divisible by
both 3 and 5 the function should write “FizzBuzz” instead of the number.
For instance, if n is 20, the program should write 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
FizzBuzz, 16, 17, Fizz, 19, and Buzz on twenty successive lines.
'''

def challenge39(n):

    for n in range(1,n+1):
        if n % 3 == 0 and n % 5 == 0:
            print  'FizzBuzz'
        elif n % 3 == 0:
            print 'Fizz'
        elif n % 5 == 0:
            print 'Buzz'
        else:
            print n
    return None

if __name__ == "__main__":
        challenge39(20)