'''
Write a script that displays the following triangle patterns separately, one below the other. Separate each pattern from the next by one blank line. Use for loops to generate the patterns. Display all asterisks (*) with a single statement of the form

    print('*', end='')                                                   

which causes the asterisks to display side by side. [Hint: For the last two patterns, begin each line with zero or more space characters.]

   (a)           (b)           (c)           (d)
   *             **********    **********             *
   **            *********      *********            **
   ***           ********        ********           ***
   ****          *******          *******          ****
   *****         ******            ******         *****
   ******        *****              *****        ******
   *******       ****                ****       *******
   ********      ***                  ***      ********
   *********     **                    **     *********
   **********    *                      *    **********
'''

print('(a)')

for i in range(1,11):
    for j in range(i):
        print('*', end='')
    print()

print()
print('(b)')

for i in range(1,11):
    for j in range(11-i):
        print('*', end='')
    print()

print()
print('(c)')

for i in range(11):
    for j in range(i):
        print(' ', end='')
    for k in range(10-i):
        print('*', end='')
    print()

print()
print('(d)')

for i in range(1,11):
    for j in range(10-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()
