"""
[2/16/2012] Challenge #8 [easy]
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.

lyrics = '99 bottles of beer on the wall, 99 bottles of beer.
    Take one down, pass it around, 98 bottles of beer on the wall...'
"""    
for num in range(99,0,-1):
    print ('%d bottles of beer on the wall, %d bottles of beer.\
 Take one down, pass it around, %d bottles of beer on the wall.' % (num,num,(num-1))),

    
 
   
  