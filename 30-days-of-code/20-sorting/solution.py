#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swapped, totalSwaps = True, 0
ranger = n-1
while swapped:
    swapped = False
    for i in range(ranger):
        if a[i] > a[i+1]:
            a[i], a[i+1], swapped = a[i+1], a[i], True
            totalSwaps += 1
    ranger -= 1
print(
    f'Array is sorted in {totalSwaps} swaps.',
    f'First Element: {a[0]}',
    f'Last Element: {a[-1]}',
sep='\n')