###############################################################################
#                                Exercice 4.13                                #
###############################################################################
#                                                                             #
# Calculate the product of a series of integers that passed to the function   #
# product, which receives an arbitrary argument list. Test your function with #
# several calls, each with a different number of arguments.                   #
#                                                                             #
###############################################################################


def product(*integers):
    total = 1
    for integer in integers:
        total *= integer
    return total

list1 = [1,2,3]
list2 = [1,2,3,4]

print()
print(list1)
print('product(list1): ', product(*list1))

print()
print(list2)
print('product(list2): ', product(*list2))

print()
