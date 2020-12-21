#!/bin/python3

import math
arr = [float(i) for i in input().split(' ')]
p_defective = (arr[0]) /100.0
p_good = 1 - p_defective
def combo(n,r):
    res = math.pow(p_defective,r) * math.pow(p_good,n-r)
    return (math.factorial(n)/(math.factorial(r) * math.factorial(n-r)) * res)
lis = [combo(10,i) for i in range(0,3)]
print("{:.3f}".format(sum(lis)))
print("{:.3f}".format((1-sum(lis))+combo(10,2)))