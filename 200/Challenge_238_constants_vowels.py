"""
[2015-10-26] Challenge #238 [Easy] Consonants and Vowels.
Create new word following a strict pattern of consonants and vowels.
Input Description: Any string of the letters c and v, uppercase or lowercase.
Output Description: A random lowercase string of letters in which consonants (bcdfghjklmnpqrstvwxyz) occupy the given 'c'
indices and vowels (aeiou) occupy the given 'v' indices.
"""
import random

def word(string):
	alphabet = {"v": "bcdfghjklmnpqrstvwxyz",
				"c": "aeiou"}
	return "".join(random.choice(alphabet[letter]) for letter in string)

print word("cvvvvvvv")

