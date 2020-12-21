# Use Python statistics module:
import statistics as stats

N = int(input())
X = list(map(int, input().split()))

print("{0:.1f}".format(stats.pstdev(X)))

