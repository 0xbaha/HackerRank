#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(n):
        if(i == 0):
            continue
        for j in range(0, i):
            if(arr[j] > arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            else:
                continue
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
