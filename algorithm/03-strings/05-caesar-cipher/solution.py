#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    a = [ord(i) for i in s ]
    for i in range(len(a)):
        if (65<=a[i]<=90) or (97<=a[i]<=122):
            if ((k%26)+a[i]>122 and 97<=a[i]<=122) or ((k%26)+a[i]>90 and 65<=a[i]<=90):
                a[i]-=26
            a[i]=(k%26)+a[i]
    return  ''.join(chr(i)for i in a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
