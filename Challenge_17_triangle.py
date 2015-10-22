'''
[3/4/2012] Challenge #17
write an application which will print a triangle of stars of user-specified height, with each line
having twice as many stars as the last. sample output:
@
@@
@@@@
hint: in many languages, the "+" sign concatenates strings.
bonus features: print the triangle in reverse, print the triangle right justified
'''
def print_stars(height):
    stars = '@'
    for row in range(height):
       print stars * 2**row
       
    for row in reversed(range(height)):
       print stars * 2**row  
       
    for row in range(height):
        maks = 2 ** (height-1)
        k = 2 ** row
        print ' ' * (maks - k) + stars * k   
            
       
print_stars(5)       