#!/bin/python3

_, a = (input(), set(input().split()))
_, b = (input(), set(input().split()))
print(len(a-b))