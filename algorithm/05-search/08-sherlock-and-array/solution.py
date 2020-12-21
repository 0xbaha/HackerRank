#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    left = []
    right = []
    sum = 0
    
    # Store sums of elements from left
    for x in arr:
        sum += x
        left.append(sum)
    sum = 0
    
    # Store sums of elements from right
    for i in range(len(arr)-1, -1, -1):
        sum += arr[i]
        right.append(sum)
    right = list(reversed(right))
    
    # Check for a common element
    for i in range(len(arr)):
        if left[i] == right[i]:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
