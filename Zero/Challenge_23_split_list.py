'''
[3/13/2012] Challenge #23 [easy]
Input: a list
Output: Return the two halves as different lists.
If the input list has an odd number, the middle item can go to any of the list.
Your task is to write the function that splits a list in two halves.
'''

lst = ["a", "b", "c", 1, 4, "x", 34, "4", "z"]

def challenge23(lst):
    return lst[:len(lst)/2], lst[len(lst)/2:]


if __name__ == "__main__":
    print challenge23(lst)