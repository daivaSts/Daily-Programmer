"""
[2015-01-19] Challenge #198 [Easy] Words with Enemies
Okay so there is a valley. On each side you got cannons. They are firing words at each other. In the middle of the valley
the words would make contact and explode. Similar letters from each word would cancel out. But the left over unique letters
from each word would fall to the valley and slowly fill it up.
The challenge is to come up with the code given two words you eliminate letters in common at a ratio of 1 for 1
and produce a set of letters that are left over from each word after colliding in mid air. Which ever side has the most letters
left over "wins". If each side donates an equal amount of letters it is a "tie".
"""

left_valley = 'haatt'
right_valley ='cata'

for letter in left_valley:
    if letter in right_valley:
        left_valley = left_valley.replace(letter,'',1)
        right_valley = right_valley.replace(letter,'',1)

if len(left_valley) == len(right_valley):
    print (left_valley, right_valley, "It's a Tie")
elif len(left_valley) > len(right_valley):
    print (left_valley, right_valley, 'Left Valley won!!!')
else:
    print  (left_valley, right_valley, 'Right Valley won!!!')
