#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    count = -64
    row = 0
    col = 0
    while row < 4 :
        temp = arr[row][col] + arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1] + arr[row+2][col]+arr[row+2][col+1]+ arr[row+2][col+2]
        if temp > count:
            count = temp
        col +=1
        if col == 4:
            col = 0
            row +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
