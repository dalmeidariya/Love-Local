#Given a string s consisting of words and spaces, return the length of the last word in the string.
def length_last_word():
    s=input('enter the string\n')
    words=s.strip().split()
    if words :
        last_word=words[-1]
        return len(last_word)
    else :
        return 0
length=length_last_word()
print ('length is ', length)

'''Steps:
Define a lengh_last_word() function to contain the main logic.
Take input and store it in s variable.
Strip, split into words, get last word length like before.
Return length or 0 if no words.
Call the function and store result in length.
Print out the length .'''