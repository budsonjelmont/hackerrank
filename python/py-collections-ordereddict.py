#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
from collections import OrderedDict
import re

if __name__=='__main__':
    regex = re.compile('^(.*) ([0-9]+)$')
    n = int(input())
    orddict = OrderedDict()
    for i in range(0,n):
        l = input()
        parsed = regex.match(l)
        item = parsed.groups(1)[0]
        val = parsed.groups(1)[1]
        try:
            orddict[item] = orddict[item] + int(val)
        except KeyError:
            orddict[item] = int(val)
    for k,v in orddict.items():
        print(f'{k} {v}') 