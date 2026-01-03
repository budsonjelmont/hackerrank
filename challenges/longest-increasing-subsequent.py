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

def longestIncreasingSubsequence(arr):
    longest_subsequences = []
    lens_longest_subsequences = []
    for i in range(len(arr)):
        longest_subsequences += [[arr[i]]]
        lens_longest_subsequences += [1]
        for j in range(i):
            if arr[i] > arr[j]:
                if lens_longest_subsequences[j] >= lens_longest_subsequences[i]:
                    longest_subsequences[i] = longest_subsequences[j] + [arr[i]]
                    lens_longest_subsequences[i] = lens_longest_subsequences[j] + 1
    len_longest_subsequence = 0
    longest_subsequence = []
    for k in longest_subsequences:
        len_current = len(k)
        if len_current > len_longest_subsequence:
            len_longest_subsequence = len_current
            longest_subsequence = k
    return len(longest_subsequence)

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
