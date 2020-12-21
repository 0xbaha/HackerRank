# Use numpy:
import numpy as np

N = int(input())
X = list(map(int, input().split())) # or X = np.array(input().split(), int)

print("{0:.1f}".format(np.std(X)))