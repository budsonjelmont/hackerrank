#https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
import time
import calendar
import re

# Complete the time_delta function below.
def time_delta(t1, t2):
    dtformat = '%a %d %B %Y %H:%M:%S %z'
    offsetformat = '.*([-+]{1})([0-9]{2})([0-9]{2})$'
    offsetre = re.compile(offsetformat)
    t1t = time.strptime(t1, dtformat)
    t1offset = offsetre.match(t1)
    t2t = time.strptime(t2, dtformat)
    t2offset = offsetre.match(t2)
    t1offsetsign, t1offsethr, t1offsetmin = (t1offset.groups(1)[0], t1offset.groups(1)[1], t1offset.groups(1)[2])
    t2offsetsign, t2offsethr, t2offsetmin = (t2offset.groups(1)[0], t2offset.groups(1)[1], t2offset.groups(1)[2])
    print(t1offsetsign)
    print(t2offsetsign)
    print(t1offsethr)
    print(t2offsethr)
    print(t1offsetmin)
    print(t2offsetmin)
    t1eptime = calendar.timegm(t1t) + int(t1offsethr) * (60**2) + int(t1offsetmin) * 60 if t1offsetsign == '+' else calendar.timegm(t1t) - (int(t1offsethr) * (60**2) + int(t1offsetmin) * 60)
    t2eptime = calendar.timegm(t2t) + int(t2offsethr) * (60**2) + int(t2offsetmin) * 60 if t2offsetsign == '+' else calendar.timegm(t2t) - (int(t2offsethr) * (60**2) + int(t2offsetmin) * 60)
    return(str(abs(t1eptime - t2eptime)))      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
