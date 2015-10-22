'''
[2/23/2012] Challenge #14 [easy]
Input: list of elements and a block size k or some other variable of your choice
Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.

For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.
'''

lst = [12, 24, 32, 44, 55, 66]

def  block_reversed(lst, k):
    result = []
    for num in range(0,len(lst),k):
        block = lst[num:(num+k)]
        
        for i in reversed(block):
            result.append(i)
    return result            
            
            
print block_reversed(lst, 3)            