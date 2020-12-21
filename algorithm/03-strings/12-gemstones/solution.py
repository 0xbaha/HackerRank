#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    min_len=min(list(map(len,arr)))
    gem=0
    for i in arr:
        if(len(i)==min_len):
            min_word=i
            break
    print(min_word)
    for i in min_word:
        fl=1
        for j in range(len(arr)):
            k=list(arr[j])
            if i not in k:
                fl=0
                break
            else:
                del k[k.index(i)]
                arr[j]="".join(k)
        if(fl==1):
            gem+=1
    return gem
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
