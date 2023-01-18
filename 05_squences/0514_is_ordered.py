'''
Create a function is_ordered that receives a sequence and returns True if the
elements are in sorted order. Test your function with sorted and unsorted lists,
tuples and strings.
'''


def is_ordered(squence):
    for i in range(len(squence)-1):
        if squence[i] > squence[i+1]:
            return False
    return True


list = ["orange", "red", "yellow"]
print(is_ordered(list), list)

list = ["red", "orange", "yellow"]
print(is_ordered(list), list)

tuple = (1, 2, 3)
print(is_ordered(tuple), tuple)

tuple = (1, 3, 2)
print(is_ordered(tuple), tuple)

string = "abcd"
print(is_ordered(string), string)

string = "abdc"
print(is_ordered(string), string)
