"""
 Challenge #3  Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!

>>>cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3)
XYZABCDEFGHIJKLMNOPQRSTUVW

>>>decipher('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD',3)
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
"""
import string 
string.ascii_letters

def cipher2(text, shift=13):
    
    alphabetUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetLow = 'abcdefghijklmnopqrstuvwxyz'
    rotateUp = alphabetUp[-shift:] + alphabetUp[:-shift]
    rotateLow = alphabetLow[-shift:] + alphabetLow[:-shift]
    result = ''

    for letter in text:
        
        if letter in alphabetUp:
            letterIndex = alphabetUp.find(letter)
            result += rotateUp[letterIndex]
        elif letter in alphabetLow:
            letterIndex = alphabetLow.find(letter)
            result += rotateLow[letterIndex]         
        else:
            result += letter            
    
    return result  
print cipher2('Hello', shift=13)
    
    
def cipher(text, shift):
    alphabetUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotate = alphabetUp[-shift:] + alphabetUp[:-shift]
    result = ''

    for letter in text.upper():
        if letter in alphabetUp:
            letterIndex = alphabetUp.find(letter)
            result += rotate[letterIndex]
        else:
            result += letter            
    
    return result     

print cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3)

def decipher(text, shift):    
    alphabetUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotate = alphabetUp[shift:] + alphabetUp[:shift]
    result = ''

    for letter in text.upper():
        if letter in alphabetUp:
            letterIndex = alphabetUp.find(letter)
            result += rotate[letterIndex]
        else:
            result += letter            
    
    return result
    
print decipher('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD',3)    