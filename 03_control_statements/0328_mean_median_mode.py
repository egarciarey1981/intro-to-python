###############################################################################
#                                Exercice 3.28                                #
###############################################################################
#                                                                             #
# Calculate the mean, median and mode of the values 9,11,22,34,17,22,34,22    #
# and 40. Suppose the values included another 34. What problem might occur?   #
#                                                                             #
###############################################################################

import statistics

values = [9,11,22,34,17,22,34,22]
print()
print(values)
print('mean  :', statistics.mean(values))
print('median:', statistics.median(values))
print('mode  :', statistics.mode(values))

values.append(34)
print()
print(values)
print('mean  :', statistics.mean(values))
print('median:', statistics.median(values))
print('mode  :', statistics.mode(values))

print()