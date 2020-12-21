# Using basic math:
import math

N = int(input())
X = list(map(int, input().split()))

mean = sum(X)/N
variance = sum([((x - mean) ** 2) for x in X]) / N
print("{0:.1f}".format(math.sqrt(variance)))