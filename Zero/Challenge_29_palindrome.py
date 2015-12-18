'''
[3/22/2012] Challenge #29 [easy]
A Palindrome is a sequence that is the same in reverse as it is forward.
I.e. hannah, 12321.
Your task is to write a function to determine whether a given string is palindromic or not.
Bonus: Support multiple lines in your function to validate Demetri Martin's 224 word palindrome poem.
'''

def challenge29(string):
    for i in range(len(string) / 2):

        if string[i] == string[-i-1]:

        	s = True
        else:
            s = False
            break
    return s

def challenge29_ignore_case(string):
    if string.lower() == string[::-1].lower():
        return True

if __name__ == "__main__":
    print challenge29('Savvas')
    print challenge29_ignore_case('Savvas')