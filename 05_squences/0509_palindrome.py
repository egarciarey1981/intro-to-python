###############################################################################
#                                Exercice 5.9                                 #
###############################################################################
#                                                                             #
# A string that’s spelled identically backward and forward, like 'radar', is  #
# a palindrome. Write a function is_palindrome that takes a string and        #
# returns True if it’s a palindrome and False otherwise. Use a stack          #
# (simulated with a list as we did in Section 5.11) to help determine whether #
# a string is a palindrome. Your function should ignore case sensitivity      #
# (that is, 'a' and 'A' are the same), spaces and punctuation.                #
#                                                                             #
###############################################################################

def is_palindrome(word):
    word = word.lower()
    stack = []

    for index in range(len(word)):
        stack.append(word[index])

    for index in range(len(word)):
        if word[index] != stack.pop():
            return False    

    return True


word = "Radar"
print(is_palindrome(word))
