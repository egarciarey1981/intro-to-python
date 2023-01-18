'''
In Exercise 2.10, you wrote a script that input three integers, then
displayed the sum, average, product, smallest and largest of those values.
Reimplement your script with a loop that inputs four integers.
'''

count = 4

sum = 0
product = 1
smallest = 999
largest = 0

for number in range(count):
    x = int(input('number '))
    sum += x
    product *= x
    smallest = min(smallest, x)
    largest = max(largest, x)

print()
print('sum     :', sum)
print('average :', sum / count)
print('product :', product)
print('smallest:', smallest)
print('largest :', largest)
