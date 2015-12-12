'''
[3/9/2012] Challenge #21 [easy]
Input: a number
Output : the next higher number that uses the same set of digits.
'''

from itertools import permutations

def challenge21(string):
    str_permutations = []

    for i in permutations(string, len(string)):
        a = ''.join(i)
        if a not in str_permutations:
            str_permutations.append(''.join(i))

    str_permutations.sort()

    if str_permutations.index(string) < len(str_permutations) - 1:
        return str_permutations[str_permutations.index(string) + 1]
    else:
        return None



if __name__ == "__main__":
        print challenge21('123')
