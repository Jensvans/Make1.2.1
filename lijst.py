#!/usr/bin/env python
"""
Een python script dat eerst een voorgeprogrammeerde lijst weergeeft, daarna om een
willekeurig aantal woorden vraagt en deze ook in een lijst steekt en weergeeft.
Dit ZONDER een loop en beroep te doen op de 'seperator'.
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


def main():
    # animals list
    animals = ['cat', 'dog', 'rabbit']

    # displays the list
    print(animals)

    # asks for more animals
    more_animals = input('type more animals here:')
    # adds to existing list
    animals.append(more_animals)
    # Updated animals list
    print('Updated animals list: ', animals)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
