#!/usr/bin/env python
"""
Vraag de gebruiker om een nummer.
Afhankelijk van het feit of het nummer even of
oneven is, print dan een passend bericht uit naar de gebruiker.
Je maakt geen gebruik van flowcontrol.
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

#asks for number
number=int(input('Enter number here:'))
#asks for multiple
multiple=int(input('Enter multiplication number here:'))


def main():
    if (number % 2) == 0:         #check if it is even
        print("{0} is Even".format(number))
    else:
        print("{0} is odd".format(number))
    if (number % 4) == 0:         #checks if it's a multiple by 4
        print("{0} is a multiple of 4".format(number))
    if (number % multiple) == 0:  #checks whether it is a multiple of the entered number
        print("{0} is a multiple of {1}".format(number, multiple))
    else:
        print("{0} is not a multiple of {1}".format(number, multiple))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
