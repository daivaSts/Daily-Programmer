"""
[2014-11-26] Challenge #190 [Intermediate] Words inside of words
Given the wordlist enable1.txt, you must find the word in that file which also contains the greatest number of
words within that word. wordsFor example, the word 'grayson' has the following words in it:
[Grayson, Gray, Grays, Ray, Rays, Son, On]
"""

words = open('enable2.txt','r')
complete_list = []
for word in words:
    complete_list.append(word[:-1])

complete_list.sort(key = len,reverse=True)
best = []
best_word = ''
best_so_far_word = ''
list_len = 0
for word1 in complete_list:
    count = 0
    best_so_far = []
    for word2 in complete_list:

        if word2 in word1:
            best_so_far.append(word2)

        best_so_far_word = word1

    if len(best_so_far) > len(best):
         best = best_so_far
         best_word = best_so_far_word
    list_len += 1
    complete_list = complete_list[list_len:]

print best_word
print best
print len(best)
words.close()
