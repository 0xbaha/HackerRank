#!/bin/python3

import math

def geometric_dist(p,n):
    return math.pow(1-p,n-1) * p

num,den = list(map(int, input().split()))
p=num/den
n = int(input())

print(round(geometric_dist(p=p, n=n), 3))