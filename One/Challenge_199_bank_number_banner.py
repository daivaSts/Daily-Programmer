'''
[2015-1-26] Challenge #199 Bank Number Banners Pt 1
You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in by branch offices.
The machine scans the paper documents, and produces a file with a number of entries which each look like this:
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number written using pipes
and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9.
Right now you're working in the print shop and you have to take account numbers and produce those paper documents.
'''

digits = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ','  |','  |'],
        '2': [' _ ',' _|','|_ '],
        '3': [' _ ',' _|',' _|'],
        '4': ['   ','|_|','  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ','|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ','|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|']
}
log = open('Bank_log.txt','w')

acct = '490067715'

for i in range(3):
    string = ''
    for j in acct:
        string += digits[j][i]
    print string

    log.write(string +'\n')


log.close()
