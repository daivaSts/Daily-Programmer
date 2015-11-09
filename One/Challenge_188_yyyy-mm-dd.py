'''
[2014-11-10] Challenge #188 [Easy] yyyy-mm-dd
iso 8601 standard for dates tells us the proper way to do an extended day is yyyy-mm-dd
yyyy = year
mm = month
dd = day
They could be one of 6 different formats:
yyyy-mm-dd
mm/dd/yy
mm#yy#dd
dd*mm*yyyy
(month word) dd, yy
(month word) dd, yyyy
(month word) can be: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Years only go between 1950-2049.
'''
import datetime
def convert_dates(d):
    # str --> yyyy-mm-dd
    months = {'Mar': 3, 'Feb': 2, 'Aug': 8, 'Sep': 9, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Jan': 1, 'May': 5, 'Nov': 11, 'Dec': 12, 'Oct': 10}

    if '-' in d:
        [year,month,day] = str(d).split('-') #yyyy-mm-dd

    elif '/' in d:
        [month,day,year] = str(d).split('/') #mm/dd/yy

    elif '#' in d:
        [month,year,day] = str(d).split('#') #mm#yy#dd

    elif '*' in d:
        [day,month,year] = str(d).split('*') #dd*mm*yyyy

    elif ' ' in d:
        [month,day,year] = str(d).split(' ') #(month word) dd, yy,  (month word) dd, yyyy Jan 09, 1983
        day = day[:-1]
        month =months[month]

    if len(year) == 2 and int(year) >= 50:
        year = '19'+year
    elif len(year) == 2 :
        year = '20'+year

    return datetime.date(int(year),int(month),int(day))



dates = open('dates.txt', 'r')

for line in dates.readlines():
    if line[-1] == '\n':
        print convert_dates(line[:-1])
    else:
        print convert_dates(line)

dates.close()
