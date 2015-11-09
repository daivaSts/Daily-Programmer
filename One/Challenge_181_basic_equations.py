'''
[09/22/2014] Challenge #181 [Easy] Basic Equations
Your task is, given two linear-style equations, find out the point at which they intersect.
Input:
You will be given 2 equations, in the form y=ax+b, on 2 separate lines, where a and b are constants
and y and x are variables.
Output:
You will print a point in the format (x, y), which is the point at which the two lines intersect.

y=2x+2
y=5x-4

(2, 6)

y=-5x
y=-4x+1

(-1, 5)
'''
def basik_equations(a1,b1,a2,b2):
    x = 0

    x = (b2-b1)/(a1-a2)
    y = a1*x+b1
    return (x,y)

print basik_equations(-5,0,-4,1)






