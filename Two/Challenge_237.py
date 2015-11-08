"""
My keyboard is broken, only a few keys work any more. If I tell you what keys work, can you tell me what words I can write?
You'll be given a line with a single integer on it, telling you how many lines to read. Then you'll be given that many lines,
 each line a list of letters representing the keys that work on my keyboard. Example:
3
abcd
qwer
hjklo

Output Description:
Your program should emit the longest valid English language word you can make for each keyboard configuration.
abcd = bacaba
qwer = ewerer
hjklo = kolokolo

Challenge Output:
edcf = deedeed
bnik = bikini
poil = pililloo
vybu = bubby
"""
text_file= open('enable1.txt','r')


def chalenge237(string):
	word = ''
	count = 0
	longest_sofar = 0
	longest_word = ''
	for line in text_file.readlines():

		line = line[:-1]

		for letter in line:

			if letter in string:
				state = True
			else:
				state =  False
				break

		if state == True:
			word = line
			count = len(line)
			if count >= longest_sofar:
				longest_word = word
				longest_sofar = count

	return (string + " = " +longest_word)



print chalenge237("edcf")
text_file.close()