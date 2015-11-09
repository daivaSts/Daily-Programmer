'''
[10/20/2014] Challenge #185 [Easy] Generated twitter handles
Both outputs should contain the 'truncated' version of the word and the original word. For example.
@tack : attack
There are two outputs that we are interested in:
The 10 longest twitter handles sorted by length in descending order.
The 10 shortest twitter handles sorted by length in ascending order.
'''
words = open('enable2.txt','r')

longest = []
shortest = []
for word in words:
    if 'at' in word:
        z = word[:-1].replace('at', '@')

        if len(longest) < 10:
            longest.append('%s : %s'%(z,word[:-1]))
        else:
            longest = sorted(longest,key=len,reverse=True)

            if len(z) > len(longest[-1]):
                longest[-1] = '%s : %s'%(z, word[:-1])

        if len(shortest) < 10:
            shortest.append('%s : %s'%(z, word[:-1]))
        else:
            shortest = sorted(shortest, key=len, reverse=False)

            if len(z) > len(shortest[-1]):
                shortest[-1] = '%s : %s'%(z, word[:-1])

for i in  shortest:
    print i


for i in  longest :
    print i
words.close()