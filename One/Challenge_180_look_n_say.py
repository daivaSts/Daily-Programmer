'''
[9/15/2014] Challenge#180 [Easy] Look'n'Say
The Look and Say sequence is an interesting sequence of numbers where each term is given by describing the makeup of the previous term.
The 1st term is given as 1. The 2nd term is 11 ('one one') because the first term (1) consisted of a single 1.
The 3rd term is then 21 ('two one') because the second term consisted of two 1s. The first 6 terms are:
1
11
21
1211
111221
312211
13112221
Input: On console input you should enter a number N
Output": e Nth Look and Say number.
'''
string = "1"
result = ""
start = "1"
count = 0
total_result = ""
Look_and_Say_number = 9
num = 0
while num < Look_and_Say_number:
	for i in range(len(string)):
		if len(string) == 1:
			total_result = '1' + string

		else:
			if string[i] == start:
				count += 1
				result = str(count) + string[i]
				#the last char in the string
				if len(string[:i + 1]) == len(string):
					total_result += result

			else:
				total_result += result
				start = string[i]
				count = 1
				result = str(count) + string[i]
				#the last char in the string
				if len(string[:i + 1]) == len(string):
					total_result += result

	print total_result
	string = total_result
	result = ""
	start = "1"
	count = 0
	total_result = ""
	num += 1




