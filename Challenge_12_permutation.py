'''
Challenge #12 [easy]
Write a small program that can take a string:
"hi!"
and print all the possible permutations of the string:
"hi!"
"ih!"
"!hi"
"h!i"
"i!h"
'''
import itertools

string = 'hi!'
z = itertools.permutations(string)
for i in itertools.permutations(string):
    print ''.join(i)
