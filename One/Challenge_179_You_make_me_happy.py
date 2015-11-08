'''
[9/08/2014] Challenge #179 [Easy] You make me happy when clouds are gray...scale
There are several methods to convert an image to grayscale, the easiest is to sum up all of the RGB values and divide it by 3
(The length of the array) and fill each R,G and B value with that number.
For example
RED = (255,0,0)
Would turn to
(85,85,85)       //Because 255/3 == 85.
'''
import Image
img = Image.open('CSSh1G5.png').convert('LA')
img.save('greyscale.png')
print img.mode, img.size