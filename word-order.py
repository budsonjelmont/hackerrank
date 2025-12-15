#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
from collections import OrderedDict

if __name__=='__main__':
    n=int(input())
    d = OrderedDict()
    for i in range(0,n):
        word = input()
        try:
            d[word]+= 1
        except KeyError:
            d[word] = 1
    print(len(d.keys()))
    for k,v in d.items():
        print(v,end=' ')
