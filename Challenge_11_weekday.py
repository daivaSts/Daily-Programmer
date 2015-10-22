'''
[2/19/2012] Challenge #11 [easy]
The program should take three arguments. The first will be a day, the second will be month,
and the third will be year. Then, your program should compute the day of the week that date
will fall on.
'''
from datetime import date

def get_weekday(year,month, day):    

    weekdays = {0:'Monday',
        1:'Tusday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'}

    ans =  date(year,month, day).weekday()
    
    return weekdays[ans]

print weekday(1964,5,8)



