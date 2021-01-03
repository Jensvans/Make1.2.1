#!/usr/bin/env python
"""
Een python script dat het volgende doet:
vraagt achter je leeftijd
berekent in welk jaar je geboren bent en dat ook als output meegeeft
berekent in welk jaar je 100 jaar zal zijn en dat ook als output meegeeft
"""


import datetime

__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


def main():
    # vraagt achter je leeftijd
    age = input('Enter your current age:')
    year = datetime.datetime.now().year
    # berekent in welk jaar je geboren bent
    year_of_birth = float(year) - float(age)
    print('year of birth =', year_of_birth)
    # berekent in welk jaar je 100 bent
    year_100 = float(year_of_birth) + (100)
    print('year you turn 100 =', year_100)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
