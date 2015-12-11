'''
[4/19/2012] Challenge #41 [easy]
Write a program that will accept a sentence as input and then output that sentence surrounded by some
type of an ASCII decoratoin banner.
Sample run:
Enter a sentence: So long and thanks for all the fish
Output
*****************************************
*                                       *
*  So long and thanks for all the fish  *
*                                       *
*****************************************
Bonus: If the sentence is too long, move words to the next line.
'''

def challenge41(sentence):
    length = len(sentence)


    if length > 40:
        print '*' * 46
        print '*' + ' ' * 44  + '*'
        sentence_folds = range(1, len(sentence)/40+2)

        for num in sentence_folds:
            sentence_part = len(sentence[40 *(num - 1): 40 * num])
            gap = 46 - sentence_part - 4
            print '*' + ' '*2 + sentence[40 *(num - 1): 40 * num]  + ' ' * gap +'*'


        print '*' + ' ' * 44  + '*'
        print '*' * 46

    else:
        print '*' * (length + 6)
        print '*' + ' ' * (length + 4) + '*'
        print '*' + ' ' * 2 + sentence + ' ' * 2 + '*'
        print '*' + ' ' * (length + 4) + '*'
        print '*' * (length + 6)


if __name__ == "__main__":
        challenge41('It does not matter how slowly you go as long as you do not stop!')
