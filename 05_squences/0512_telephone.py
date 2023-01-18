'''
(Telephone-Number Word Generator) You should find this exercise to be
entertaining. Standard telephone keypads contain the digits zero through nine.
The numbers two through nine each have three letters associated with them, as
shown in the following table:

Digit   Letters
2       A B C
3       D E F
4       G H I
5       J K L
6       M N O
7       P R S
8       T U V
9       W X Y

Many people find it difficult to memorize phone numbers, so they use the
correspondence between digits and letters to develop seven-letter words (or
phrases) that correspond to their phone numbers. For example, a person whose
telephone number is 686-2377 might use the correspondence indicated in the
preceding table to develop the sevenletter word “NUMBERS.” Every seven-letter
word or phrase corresponds to exactly one seven-digit telephone number. A
budding data science entrepreneur might like to reserve the phone number
244-3282 (“BIGDATA”).

Every seven-digit phone number without 0s or 1s corresponds to many different
seven-letter words, but most of these words represent unrecognizable gibberish.
A veterinarian with the phone number 738-2273 would be pleased to know that the
number corresponds to the letters “PETCARE.”

Write a script that, given a seven-digit number, generates every possible
seven-letter word combination corresponding to that number. There are 2187 (3^7)
such combinations. Avoid phone numbers with the digits 0 and 1 (to which no
letters correspond). See if your phone number corresponds to meaningful words.
'''

keypads = [
    [],
    [],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y'],
]


def wordGenerator(phoneNumber):
    phoneNumber = str(phoneNumber)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        for f in range(3):
                            for g in range(3):
                                print(
                                    keypads[int(phoneNumber[0])][a],
                                    keypads[int(phoneNumber[1])][b],
                                    keypads[int(phoneNumber[2])][c],
                                    keypads[int(phoneNumber[3])][d],
                                    keypads[int(phoneNumber[4])][e],
                                    keypads[int(phoneNumber[5])][f],
                                    keypads[int(phoneNumber[6])][g],
                                    sep='',
                                    end=', ',
                                )


wordGenerator(2443282)
print()
