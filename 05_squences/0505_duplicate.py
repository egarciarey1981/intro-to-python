###############################################################################
#                                Exercice 5.5                                 #
###############################################################################
#                                                                             #
# Create a function that receives a list and returns a (possibly shorter)     #
# list containing only the unique values in sorted order. Test your function  #
# with a list of numbers and a list of strings.                               #
#                                                                             #
###############################################################################

def removeDuplicates(elements):
    return [elements[i] for i in range(len(elements)) if elements[i] not in elements[0:(i)]]

numbers = [1,2,2,3,3,3,1,2,2,3,3,3,]
print(numbers)

numbers = removeDuplicates(numbers)
print(numbers)