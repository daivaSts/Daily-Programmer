'''
[2015-1-26] Challenge #199 Bank Number Banners Pt 2
Now, when we purchased these fax machines and wrote the programme to enable us to send numbers to our machine,
we realised something... We couldn't translate it back! This meant that sending a fax of this number format was
useless as no one could interpret it.
Your job is to parse back the fax numbers into normal digits.
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

log1 = open('Bank_log2.txt','w')
acct = '490067715'


# translate numbers to electronic machine format
for i in range(3):
    string = ''
    for j in acct:
        string += digits[j][i]

    log1.write(string +'\n')
log1.close()


# translate it back:
log2 = open('Bank_log1.txt','r')

# create dict with empty values
diggits2 = {}
for count in range(len(acct)):
    diggits2[count] = ''

# read file w/electronic machine digits
for line in log2.readlines():

    count = 0
    while(count<9):
        diggits2[count] += line[0:3]
        line = line[3:]
        count += 1

# create list and split value string into 3 - 3 char strings
n = 3
i = 0
for j in range(len(diggits2)):
    diggits2[j] = [diggits2[j][i:i+n] for i in range(0, len(diggits2[j]), n)]
    print diggits2[j]


result = ''
for index, num in enumerate(acct):
    for key, value in digits.items():
        if diggits2[index] == value:
            result += key

#print result
log2.close()
