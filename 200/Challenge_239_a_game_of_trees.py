"""
[2015-11-02] Challenge #239 [Easy] A Game of Threes
The input is a single number: the number at which the game starts. Write a program that plays the Threes game,
and outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you
start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing).
The last line should simply be 1.
The input is a single number: the number at which the game starts.
100
The output is a list of valid steps that must be taken to play the game. Each step is represented by the number you start at,
followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing).
The last line should simply be 1.
100 -1
33 0
11 1
4 -1
1
"""
def game_of_trees(n):
	if n == 1:
		print 1
	while n != 1:
		if n % 3 == 0:
			print n, 0
			n = n/3
		elif (n + 1) % 3 == 0:
			print n, 1
			n = (n + 1)/3
		elif (n - 1) % 3 == 0:
			print n, -1
			n = (n - 1)/3
		else:
			"error"
	print 1

game_of_trees(31337357)

