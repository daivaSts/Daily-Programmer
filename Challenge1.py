"""
Reddit chalenge # 1 easy

program that asks the users name, age, and reddit username. 
tell them the information back, in the format:
*your name is (blank), you are (blank) years old, and your username is (blank)*
and log this information in a file to be accessed later.
"""

name = raw_input("What is your name?")
age = raw_input("What is your age?") 
username = raw_input("What is your username?")

user_info = 'your name is %s, you are %d years old, and your username is %s' %(name, int(age), username)


with open('user_log.txt', 'a') as the_file:
    the_file.write(user_info)
    the_file.write('\n')
       

#testing = open('user_log.txt', 'r')
#
#for line in  testing.readlines():
#    print line