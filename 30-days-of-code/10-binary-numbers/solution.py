#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    num = bin(n)[2:]
    l = str(num).split("0")
    c = len(max(l))
    print(c)
