"""
Calenge # 4 Random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""
import random
import string


lenght = raw_input('Enter how long you want your password -> ')
populiation = string.letters

password1  = ''.join([random.choice(populiation) for _ in range(int(lenght))])
print password1

password2 = ''.join(random.sample(populiation,5))
print password2
