#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# return first element >= query
def binary_search(qry, arr):
    l = 0
    r = len(arr)-1
    while l <= r:
      m = (r+l)//2
      if qry == arr[m]:
          return m
      elif qry > arr[m]:
          l = m + 1
      elif qry < arr[m]:
          r = m - 1
    return l

def longestIncreasingSubsequence(arr):
    res = [arr[0]]
    for i in range(1,len(arr)):
        # extend the result array by 1 if this number would extend the subsequence
        if arr[i] > res[-1]:
            res.append(arr[i])
        # otherwise, replace the smallest number in the result array that's greater than the number
        else:
            # binary search for element to replace
            replace_me = binary_search(arr[i],res) # returns index of smallest number >= the query 
            res[replace_me] = arr[i]
    return len(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
