#!/bin/python3

n = int(input())
s = set()
for i in range(n):
    string = input()
    s.add(string)
print(len(s))