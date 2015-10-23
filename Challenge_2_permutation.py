"""
Reddit chalenge # 2 easy

Write a small program that can take a string: "hi!"
and print all the possible permutations of the string
"""
from itertools import permutations

perms = [''.join(p) for p in permutations("hi!")]

print perms


#itertools.permutations(iterable[, r])
#Return successive r length permutations of elements in the iterable.
#If r is not specified or is None, then r defaults to the length of the iterable and all
#possible full-length permutations are generated.
#Permutations are emitted in lexicographic sort order. 
#So, if the input iterable is sorted, the permutation tuples will be produced in sorted order.