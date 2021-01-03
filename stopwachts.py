#!/usr/bin/env python
"""
Info
"""

import time


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


def Timer(sec):
  min = sec // 60
  sec = sec % 60
  hours = min // 60
  min = min % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(min),sec))#this prints in hours minutes and seconds

#this start the Stopwach
input("Press Enter to start")
start_time = time.time()

#this stops het Stopwach
input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
Timer(time_lapsed)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
