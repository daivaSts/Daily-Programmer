'''
[2015-02-09] Challenge #201 [Easy] Counting the Days until...
So today let us do some calendar math. Given a date that is in the future
how many days until that date from the current date?
Example Input: 2015 2 14
Example Output: 5 days from 2015 2 9 to 2015 2 14
Challenge Inputs:

 2015 7 4
 2015 10 31
 2015 12 24
 2016 1 1
 2016 2 9
 2020 1 1
 2020 2 9
 2020 3 1
 3015 2 9
'''
import  datetime

def counting_days(date1,date2):
    year1,month1,day1 = date1.split(' ')
    year2,month2,day2 = date2.split(' ')

    date1 =  datetime.date(int(year2),int(month2),int(day2))
    date2 = datetime.date(int(year1),int(month1),int(day1))

    t =  str(date1-date2)

    return '%s days from %s  to %s' %(t.split(' ')[0], date2, date1)

print counting_days('2012 05 01','2012 05 28')


