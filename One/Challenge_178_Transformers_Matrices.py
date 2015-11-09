'''
Challenge #178 [Easy] Transformers: Matrices in Disguise, pt. 1

We'll be writing a program which will take a point in 2-dimensional space, represented as (X, Y) (where X and Y can be decimal and negative),
transform them a number of times in different ways and then find the final position of the point.
Your program must be able to do the following:

Translations - ie. offsetting the X and Y co-ordinates by a given amount http://i.imgur.com/3jI4sGI.png
Rotations by an arbitrary angle around a given point http://i.imgur.com/9c0ji7c.png
Scale relative to a point http://i.imgur.com/vHUfXv2.png
Reflection over the X or Y axis http://i.imgur.com/X6JH6pT.png
https://www.mathsisfun.com/algebra/distance-2-points.html
http://www.mathsisfun.com/algebra/trigonometry.html
'''
import math
print math.tan(30)

def offset(x,y,a,b):
    return x+a,y+b

def rotate(a,b,x,y,c):
    d = math.sqrt((x-a)**2 +(y-b)**2)
    return d

