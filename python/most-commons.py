#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

    letters={}
    for i in s:
        try:
            letters[i]+=1
        except KeyError:
            letters[i]=1

    occurs={}
    for k,v in letters.items():
        try:
            occurs[v].append(k)
        except KeyError:
            occurs[v] = [k]

    orderedoccurskeys = [k for k in occurs.keys()]
    orderedoccurskeys.sort(reverse=True)

    letterlist = []
    occurslist = []

    for k in orderedoccurskeys:
        alphasorted = occurs[k]
        alphasorted.sort()
        for a in alphasorted:
            occurslist.append(k)
            letterlist.append(a)

    for i in range(0,3):
        print(f'{letterlist[i]} {occurslist[i]}')