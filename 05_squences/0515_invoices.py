'''
When you purchase products or services from a company, you typically receive an
invoice listing what you purchased and the total amount of money due. Use
tuples to represent hardware store invoices that consist of four pieces of
data—a part ID string, a part description string, an integer quantity of the
item being purchased and, for simplicity, a float item price (in general,
Decimal should be used for monetary amounts). Use the sample hardware data
shown in the following table.

Part number     Part description    Quantity    Price
83              Electric sander     7           57.98
24              Power saw           18          99.99
7               Sledge hammer       11          21.50
77              Hammer              76          11.99
39              Jig saw             3           79.50

Perform the following tasks on a list of invoice tuples:

a) Use function sorted with a key argument to sort the tuples by part
description, then display the results. To specify the element of the tuple that
should be used for sorting, first import the itemgetter function from the
operator module as in

    from operator import itemgetter

Then, for sorted's key argument specify itemgetter(index) where index specifies
which element of the tuple should be used for sorting purposes.

b) Use the sorted function with a key argument to sort the tuples by price, then
display the results.

c) Map each invoice tuple to a tuple containing the part description and
quantity, sort the results by quantity, then display the results.

d) Map each invoice tuple to a tuple containing the part description and the
value of the invoice (the product of the quantity and the item price), sort the
results by the invoice value, then display the results.

e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.

f) Calculate the total of all the invoices.
'''


from operator import itemgetter
from functools import reduce

pieces = [
    (83, "Electric sander", 7, 57.98),
    (24, "Power saw", 18, 99.99),
    (7, "Sledge hammer", 11, 21.50),
    (77, "Hammer", 76, 11.99),
    (39, "Jig saw", 3, 79.50),
]

print()
print("A - sort by description")
print("^^^^^^^^^^^^^^^^^^^^^^^")
for piece in sorted(pieces, key=itemgetter(1)):
    print(piece)

print()
print("B - sort by price")
print("^^^^^^^^^^^^^^^^^")
for piece in sorted(pieces, key=itemgetter(3)):
    print(piece)

print()
print("C - sort (description, quantity) by quantity")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for piece in sorted(map(lambda x: (x[1], x[2]), pieces), key=itemgetter(1)):
    print(piece)

print()
print("D - sort (description, invoice) by quantity")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for piece in sorted(map(lambda x: (x[1], float(f"{x[2] * x[3]:.2f}")), pieces), key=itemgetter(1)):
    print(piece)

print()
print("E - total invoice")
print("^^^^^^^^^^^^^^^^^")
print(reduce(lambda a, b: a+b, sorted(map(lambda x: x[2] * x[3], pieces))))

print()
