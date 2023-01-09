###############################################################################
#                                Exercice 3.9                                 #
###############################################################################
#                                                                             #
# In In Exercise 2.11, you wrote a script that separated a five-digit integer #
# into its individual digits and displayed them. Reimplement your script to   #
# use a loop that in each iteration “picks off” one digit (left to right)     #
# using the // and % operators, then displays that digit.                     #
#                                                                             #
###############################################################################

number = int(input('number (5 digits): '))

for i in range(5):
    denominator = 10 ** (5-i-1)
    print(number // denominator, end='   ')
    number %= denominator
print()
