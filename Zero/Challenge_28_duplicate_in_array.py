'''
[3/20/2012] Challenge #28 [easy]
The array duplicates problem is when one integer is in an array for more than once.
If you are given an array with integers between 1 and 1,000,000 or in some other interval and one integer is in
the array twice. How can you determine which one?
Note: try to find the most efficient way to solve this challenge.
'''

import collections

lst = [2,6,8,6,9,12,15,19,16,25,29,30,32,16]

z = collections.Counter(lst)
print z.most_common(2)


value_dict = {}
for i,j in enumerate(lst):
	if j in value_dict:
		print "List[{}] and List[{}] value is {}".format(value_dict[j], i, lst[i])

	hashtable[j] = i

