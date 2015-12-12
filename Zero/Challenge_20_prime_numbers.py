'''
[3/8/2012] Challenge #20 [easy]
create a program that will find all prime numbers below 2000

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other
than 1 and itself. A natural number greater than 1 that is not a prime number is called a composite number.
'''
def challenge20(a, b):
	lst = range(a, b)
	copy_list = lst[:]

	for i in copy_list:
	    for j in range(2, (i)):
	        if i % j == 0:
	            lst.remove(i)
	            break

	print lst
	print len(lst)


if __name__ == "__main__":
        challenge20(2,100)