'''
[3/17/2012] Challenge #27 [easy]
Write a program that accepts a year as input and outputs the century the year belongs in (e.g. 18th century's year ranges are
1701 to 1800) and whether or not the year is a leap year.
Sample run:

Enter Year: 1996
Century: 20
Leap Year: Yes

Enter Year: 1900
Century: 19
Leap Year: No
'''

def challenge27(year):

    if year % 4 == 0:
        leap_year = True
        if year >= 400 and year % 100 == 0:
            if year % 400 == 0:
                leap_year = 'Yes'
            else:
                leap_year = 'No'
    else:
        leap_year = 'No'

    if year % 100 == 0:
        return 'Century: {}, Leap Year: {}'.format(year / 100, leap_year)
    else:
        return 'Century: {}, Leap Year: {}'.format(year / 100 + 1, leap_year)

if __name__ == "__main__":
    print challenge27(1900)

