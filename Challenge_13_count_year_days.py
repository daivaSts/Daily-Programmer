# -*- coding: utf-8 -*-
'''
[2/21/2012] Challenge #13 [easy]
Find the number of the year for the given date. For example, january 1st would be 1, 
and december 31st is 365.
for extra credit, allow it to calculate leap years, as well.

A leap year consists of 366 days, as opposed to a common year, which has 365. 
Nearly every 4 years is a Leap Year, and we add a Leap Day, an extra – or intercalary – 
day on February 29.
'''

months ={'January':0,
    'February':1,
    'March':2,
    'April':3,
    'May':4,
    'June':5,
    'July':6,
    'August':7,
    'September':8,
    'October':9,
    'November':10,
    'December':11}   
      
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]    

def leapYear(year):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
        if year >= 400 and year % 100 == 0:
            if year % 400 == 0:       
                leap_year = True
            else:
                leap_year = False    
    else:
        leap_year = False
    return leap_year        
        
def count_days(year,month, day):   
      ans = sum(days_in_month[:months[month]]) + day
      if leapYear(year):
          return ans + 1
      else:    
          return ans
      
      
print count_days(2015,'June', 5)        