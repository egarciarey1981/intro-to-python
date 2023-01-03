###############################################################################
#                                Exercice 3.1                                 #
###############################################################################
#                                                                             #
# Modify the script of Fig. 3.3 to validate its inputs. For any input, if the #
# value entered is other than 1 or 2, keep looping until the user enters a    #
# correct value. Use one counter to keep track of the number of passes, then  #
# calculate the number of failures after all the user’s inputs have been      #
# received.                                                                   #
#                                                                             #
###############################################################################

student = 0
passes = 0
failures = 0

while student < 10:

    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
        student = student + 1
    elif result == 2:
        failures = failures + 1
        student = student + 1

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
