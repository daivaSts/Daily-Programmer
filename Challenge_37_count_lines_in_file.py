'''
[4/8/2012] Challenge #37 [easy]
write a program that takes
input : a file as an argument
output: counts the total number of lines.
for bonus, also count the number of words in the file.
'''
book = open('TheAdventuresofSherlockHolmes.txt','r')

lines = 0
words = 0
for line in book.readlines():
    lines += 1
    words +=  len(line.split())


print "Lines in the book: ", lines
print "Words in the book: ", words
book.close()

print ("Newlines: %s\nWords: %s" % (lines, words))