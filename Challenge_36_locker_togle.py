'''
[4/5/2012] Challenge #36 [easy]
1000 Lockers Problem.
In an imaginary high school there exist 1000 lockers labelled 1, 2, ..., 1000. All of them are closed.
1000 students are to "toggle" a locker's state. * The first student toggles all of them *
The second one toggles every other one (i.e, 2, 4, 6, ...) * The third one toggles the multiples of 3 (3, 6, 9, ...)
and so on until all students have finished.
To toggle means to close the locker if it is open, and to open it if it's closed.
How many and which lockers are open in the end?
'''

def challenge36(n):
	lockers = range(1,n + 1)
	result = [1] * n

	for student in range (2,n + 1):
	    for locker in lockers:

	        if locker%student == 0:
	            if result[lockers.index(locker)] == 1:
	                result[lockers.index(locker)] = 0
	            else:
	                result[lockers.index(locker)] = 1

	j = 1
	for i in result:
	    if i == 1:
	        print 'locker %d is open' %j
	    j +=1

if __name__ == "__main__":
        challenge36(100)