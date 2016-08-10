#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports
def uses_all(wordtocheck,strall):
    reqletters=[]
    reqletters.extend(strall)
    flag=True
    for n in reqletters:
        flag1=n in wordtocheck
        flag=flag and flag1
    return flag
# Body

def words_use_all(filename,strall):
    filecheck=open(filename,'r')
    txt=filecheck.read().split()
    reqletters=[]
    reqletters.extend(strall)
    wordswithall='The count of words with all of the letters '+strall+' is: '
    count=0
    for words in txt:
        flag=True
        for n in reqletters:
            flag1=n in words
            flag=flag and flag1
        if flag == True:
            count=count+1
    wordswithall=wordswithall+str(count)
    print(wordswithall)



##############################################################################
def main():
    uses_all('words.txt','dsg')
    words_uses_all('words.txt','aeiou')
    words_uses_all('words.txt','aeiouy')

if __name__ == '__main__':
    main()
