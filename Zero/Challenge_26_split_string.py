'''
[3/16/2012] Challenge #26 [easy]
you have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates and put them
in a separate string, which yields two separate instances of the string "dailyprogramer".
use this list for testing:
input: "balloons"
expected output: "balons" "lo"
input: "ddaaiillyypprrooggrraammeerr"
expected output: "dailyprogramer" "dailyprogramer"
input: "aabbccddeded"
expected output: "abcdeded" "abcd"
input: "flabby aapples"
expected output: "flaby aples" "bap"
'''

string = "ddaaiillyypprrooggrraammeerr"

def challenge26(string):
    temp1 = string[0]
    temp2 = ''

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            temp2 += string[i]
        else:
            temp1 += string[i]

    return temp1, temp2


if __name__ == "__main__":
	print challenge26(string)