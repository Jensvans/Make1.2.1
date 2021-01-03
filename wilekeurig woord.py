#!/usr/bin/env python
"""
Info Een python script dat als output het aantal tekens geeft van de ingegeven string.
Het script vraagt om een willekeurig woord in te geven en geeft als output het aantal tekens terug.
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


def main():
    word=input('Type your word here:')
    word_length=len(word)
    print('The Word has {0} characters'.format(word_length))

if __name__ == '__main__':  # code to execute if called from command-line
    main()
