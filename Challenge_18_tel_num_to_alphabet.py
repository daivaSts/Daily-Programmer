'''
[3/5/2012] Challenge #18 [easy]
Often times in commercials, phone numbers contain letters so that they're easy to remember 
(e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters 
into a phone number with only numbers and the appropriate dash. Click here to learn more about the telephone keypad.
Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278
'''
keypad = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,
        'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9
         }

      
tel_alpha  =  '1-800-VERIZON' 
def tel_num(num):
    result = ''
    
    for char in num:             
        if char in keypad.keys():
            result += str(keypad[char])
        else:
            result += char
            
    if result[1] != '-':
        result = result[:1] + '-' + result[1:] 
    if result[5] != '-':
        result = result[:5] + '-' + result[5:] 
    if result[8] != '-':
        result = result[:9] + '-' + result[9:]         
    
    return result
print tel_num(tel_alpha)                                    
                
                        