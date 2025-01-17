# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
from collections import OrderedDict

def merge_the_tools(string, k):
    if len(string) % k != 0:
        exit("ERROR")
    for i in range(0,len(string),k):
        substr = string[i:i+k]
        substrdict = OrderedDict()
        for j in substr:
            substrdict[j] = True
        print(''.join(substrdict.keys()))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)