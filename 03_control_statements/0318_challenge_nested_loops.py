###############################################################################
#                                Exercice 3.18                                #
###############################################################################
#                                                                             #
# Modify your script from Exercise 3.17 to display all four patterns          #
# side-by-side (as shown above) by making clever use of nested for loops.     #
# Separate each triangle from the next by three horizontal spaces. [Hint: One #
# for loop should control the row number. Its nested for loops should         #
# calculate from the row number the appropriate number of asterisks and       #
# spaces for each of the four patterns.]                                      #
#                                                                             #
###############################################################################

print()
print('(a)', '(b)', '(c)', '(d)', sep='          ')

for i in range(1,11):
    for j in range(i):
        print('*', end='')
    for j in range(10-i+3):
        print(' ', end='')


    for j in range(11-i):
        print('*', end='')
    for j in range(i-1+3):
        print(' ', end='')


    for j in range(i-1):
        print(' ', end='')
    for j in range(11-i):
        print('*', end='')


    for j in range(10-i+3):
        print(' ', end='')
    for j in range(i):
        print('*', end='')

    print()
print()