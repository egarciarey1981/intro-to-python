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
    result = []

    while len(elements) != 0:
        element = elements[0]
        result.append(element)
        elements = [others for others in elements if others != element]

    return result

list = [1,2,3,3,2,1,2,3,3,2,2,2,1,3]

print(list)
print(removeDuplicates(list))