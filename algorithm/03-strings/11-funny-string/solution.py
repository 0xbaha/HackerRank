#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.


def funnyString(s):
    original_difference = []
    reversed_difference = []

    num = len(s)

    for x in range(num - 1):
        original_difference.append(abs(ord(s[x]) - ord(s[x + 1])))
        reversed_difference.append(
            abs(ord(s[num - 1 - x]) - ord(s[num - x - 2])))

    for x in range(len(original_difference)):
        if original_difference[x] != reversed_difference[x]:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
