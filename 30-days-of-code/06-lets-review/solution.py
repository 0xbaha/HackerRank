#!/bin/python3

for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
