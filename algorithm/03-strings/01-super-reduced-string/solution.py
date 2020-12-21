#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    newString=s[0]
    for i in range(1,len(s)):
        if newString == '' or s[i] != newString[-1]:
            newString += s[i]
        else:
            newString= newString[:-1]
    if newString == '':
        return 'Empty String'
    return newString

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    # fptr.write(result + '\n')

    # fptr.close()
