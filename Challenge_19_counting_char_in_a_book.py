'''
[3/7/2012] Challenge #19 [easy]
Challenge #19 will use The Adventures of Sherlock Holmes from Project Gutenberg.
Write a program that counts the number of alphanumeric characters there are in The Adventures of Sherlock Holmes.
Exclude the Project Gutenberg header and footer, book title, story titles, and chapters.
Post your code and the alphanumeric character count.
'''
import string


The_Adventures_of_Sherlock_Holmes = 'C:\Users\daiva\Documents\Books\The Adventures of Sherlock Holmes.txt'

book = open(The_Adventures_of_Sherlock_Holmes,'r')
count_line = 0
count_char = 0

for line in book.readlines():
    count_line += 1
    if 'II.' in line  or 'V.' in line or 'X.' in line:    
        continue
        
    if count_line > 61 and count_line < 12682:      
        for char in line:
              if char in string.ascii_letters or char in string.digits:                  
                    count_char += 1 
                                                                                                                        
print count_char    

book.close()