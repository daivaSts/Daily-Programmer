'''
[10/13/2014] Challenge #184 [Easy] Smart Stack List

Data: The smart link list will hold integer data.

The smart link list must support these methods or operations:
Push - Push a number on top of the stack (our link list is a stack)
Pop - Pop the number off the top of the stack
Size - how many numbers are on your stack
Remove Greater - remove all integers off the stack greater in value then the given number
Display Stack - shows the stack order of the list (the order they were pushed from recent to oldest)
Display Ordered - shows the integers sorted from lowest to highest.

Smart list: One could make a stack and when you do the display ordered do a sort. But our smart list must have a way so
that it takes O(n) to display the link list in stack order or ascending order. In other words our link list is always in
stack and sorted order. How do you make this work? That is the real challenge.

Test your list:

Develop a quick program that uses your smart stack list.
Generate a random number between 1-40. Call this number n.
Generate n random numbers between -1000 to 1000 and push them on your list
Display stack and sorted order
Generate a random number between -1000 and 1000 can call it x
Remove greater X from your list. (all integers greater than x)
Display stack and sorted order
Pop your list (size of list / 2) times (50% of your list is removed)
Display stack and sorted order
'''
import random
smart_list = []
n = random.randint(1,10)

for num in range(n):
    x = random.randint(-1000,1000)
    smart_list.append(x)



print smart_list
print sorted(smart_list)

x = random.randint(-1000,1000)

greater_removed = [z for z in sorted(smart_list) if z < x ]
stack_greater_removed = [a for a in smart_list if a in greater_removed ]

print greater_removed
print stack_greater_removed