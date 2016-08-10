#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(wordarg):
    return str(not 'e' in wordarg)+'\n'

def has_no_e_mod(filename):
    filecheck=open(filename,'r')
    txt=filecheck.read().split()
    wordswithoute='The words without e are: \n\n'
    for wordarg in txt:
        if not 'e' in wordarg:
            wordswithoute=wordswithoute+wordarg+'\n'
    print(wordswithoute)


##############################################################################
def main():
    print(has_no_e('hello'))
    print(has_no_e('ok'))
    has_no_e_mod('words.txt')

if __name__ == '__main__':
    main()
