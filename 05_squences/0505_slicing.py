###############################################################################
#                                Exercice 5.5                                 #
###############################################################################
#                                                                             #
# Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz',    #
# then perform the following separate slice operations to obtain:             #
#   a) The first half of the string using starting and ending indices.        #
#   b) The first half of the string using only the ending index.              #
#   c) The second half of the string using starting and ending indices.       #
#   d) The second half of the string using only the starting index.           #
#   e) Every second letter in the string starting with 'a'.                   #
#   f) The entire string in reverse.                                          #
#   g) Every third letter of the string in reverse starting with 'z'.         #                                           
#                                                                             #
###############################################################################

alphabet = "abcdefghijklmnopqrstuvwxyz"

half = len(alphabet) // 2

print("a)", alphabet[0:half])
print("b)", alphabet[:half])
print("c)", alphabet[half:len(alphabet)])
print("d)", alphabet[half:])
print("e)", alphabet[::2])
print("f)", alphabet[::-1])
print("g)", alphabet[::-2])
