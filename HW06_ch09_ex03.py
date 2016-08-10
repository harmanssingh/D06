#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(wordtocheck,strforbid):
    """ return True if word NOT forbidden"""
    forbidden=[]
    forbidden.extend(strforbid)
    flag=True
    for n in forbidden:
        flag1=not n in wordtocheck
        flag=flag and flag1
    return flag



def forbidden_prompt(filename):
    """ print count of words NOT forbidden by input"""
    filecheck=open(filename,'r')
    txt=filecheck.read().split()
    strforbid=input("Enter a string containing all forbidden letters: ")
    forbidden=[]
    forbidden.extend(strforbid)
    wordswithoute='The count of words without the letters '+strforbid+' is: '
    count=0
    for words in txt:
        flag=True
        for n in forbidden:
            flag1=not n in words
            flag=flag and flag1
        if flag == True:
            count=count+1
    wordswithoute=wordswithoute+str(count)
    print(wordswithoute)


def forbidden_param(filename,strforbid):
    """ return count of words NOT forbidden by param"""
    filecheck=open(filename,'r')
    txt=filecheck.read().split()
    forbidden=[]
    forbidden.extend(strforbid)
    wordswithoute='The count of words without the letters '+strforbid+' is: '
    count=0
    for words in txt:
        flag=True
        for n in forbidden:
            flag1=not n in words
            flag=flag and flag1
        if flag == True:
            count=count+1
    return count

def recursive_call_for_print_5(filename,chararg):
    max=0
    forb=''
    for charcheck in range(97,122):
        if chr(charcheck) in chararg:
            break
        else:
            count=forbidden_param(filename,chararg+chr(charcheck))
            if count > max:
                max = count
                forb=chr(charcheck)
    return forb

def find_five(filename):
    char1=recursive_call_for_print_5(filename,'')
    char2=recursive_call_for_print_5(filename,char1)
    char3=recursive_call_for_print_5(filename,char1+char2)
    char4=recursive_call_for_print_5(filename,char1+char2+char3)
    char5=recursive_call_for_print_5(filename,char1+char2+char3+char4)
    print("the combination of 5 forbidden words that excludes the minimum words is :"+char1+char2+char3+char4+char5)






##############################################################################
def main():
    ...
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
