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
def str_to_time(t_str):
    dtformat = '%a %d %B %Y %H:%M:%S %z'
    t_time = time.strptime(t_str, dtformat)
    return t_time

def str_to_offset(t_str):
    offsetformat = '.*([-+]{1})([0-9]{2})([0-9]{2})$'
    offsetre = re.compile(offsetformat)
    toffset = offsetre.match(t_str)
    offsetsign, offsethr, offsetmin = (toffset.groups(1)[0], toffset.groups(1)[1], toffset.groups(1)[2])
    return (offsetsign, offsethr, offsetmin)

def calculate_epoch(t_time, toffset):
    offsetsign, offsethr, offsetmin = toffset
    eptime = calendar.timegm(t_time) - (int(offsethr) * (60**2) + int(offsetmin) * 60) if offsetsign == '+' else calendar.timegm(t_time) + (int(offsethr) * (60**2) + int(offsetmin) * 60)
    return eptime

def time_delta(t1, t2):
    t1t = str_to_time(t1)
    t2t = str_to_time(t2)
    t1offsetsign, t1offsethr, t1offsetmin = str_to_offset(t1)
    t2offsetsign, t2offsethr, t2offsetmin = str_to_offset(t2)
    t1eptime = int(calculate_epoch(t1t, (t1offsetsign, t1offsethr, t1offsetmin)))
    t2eptime = int(calculate_epoch(t2t, (t2offsetsign, t2offsethr, t2offsetmin)))
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
