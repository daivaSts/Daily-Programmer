"""
[2/12/2012] Challenge #5 [easy]
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)
"""
 
user = False
password = False

user_name_request = raw_input('Enter user name ->  ')
user_name_file = open('user_names.txt', 'r')
user_name_indx = user_name_file.readlines().index(user_name_request+'\n')


if user_name_indx != -1:
    user = True

password_request = raw_input('Enter password ->  ')
password_file = open('passw.txt', 'r')

p = password_file.readlines()

if p[user_name_indx][:-1] == password_request:
    password = True
             
if user == True and password == True:
    print "Log in successful"    
else:
    print "Log in failed. User name or password is incorrect"   
    
user_name_file.close()  
password_file.close()                                                                    