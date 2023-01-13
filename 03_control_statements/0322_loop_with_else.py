###############################################################################
#                                Exercice 3.22                                #
###############################################################################
#                                                                             #
# The while and for statements each have an optional else clause. In a while  #
# statement, the else clause executes when the condition becomes False. In a  #
# for statement, the else clause executes when there are no more items to     #
# process. If you break out of a while or for that has an else, the else part #
# does not execute. Execute the following code to see that the else clause    #
# executes only if the break statement does not:                              #
#                                                                             #
#       for i in range(2):                                                    #
#           value = int(input('Enter an integer (-1 to break): '))            #
#           print('You entered:', value)                                      #
#                                                                             #
#           if value == -1:                                                   #
#               break                                                         # 
#       else:                                                                 #
#           print('The loop terminated without executing the break')          #
#                                                                             #
###############################################################################

for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)
    if value == -1:
        break
else:
    print('The loop terminated without executing the break')   