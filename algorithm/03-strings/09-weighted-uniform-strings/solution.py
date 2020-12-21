#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    a=ord(s[0])-96
    leng=set()
		
    #An extra random character used as an
    #extra iteration or else the last character is not 
    #getting considered
    s=s+"_"
    for i in range(1,len(s)):
        leng.add(a)
        if s[i]==s[i-1]:   
            a+=(ord(s[i])-96)
        else:
            a=(ord(s[i])-96)
    return ["Yes" if i in leng else "No" for i in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
