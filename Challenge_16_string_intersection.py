# -*- coding: utf-8 -*-
'''
[2/27/2012] Challenge #16 [easy]
Write a function that takes two strings and removes from the first string any character that appears in
the second string. For instance, if the first string is “Daily Programmer” and the second string is “aeiou ”
the result is “DlyPrgrmmr”.
note: the second string has [space] so the space between "Daily Programmer" is removed
'''

str1 = 'Daily Programmer'
str2 = 'aeiou '


print ''.join([i for i in str1 if i not in str2])
