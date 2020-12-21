#!/bin/python3

n,m = input().split()
arr = input().split()
L = set(input().split())  # like
D = set(input().split())  # dislike
print(sum((i in L) - (i in D) for i in arr))