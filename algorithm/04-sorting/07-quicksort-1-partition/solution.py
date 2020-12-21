#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.


def quickSort(arr):
    left, equal, right = [], [], []
    pivot = arr[0]
    for i in arr:
        if i == pivot:
            equal.append(i) 
        elif i > pivot:
            right.append(i) 
        elif i < pivot:
            left.append(i) 
    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
