x,s = int(input()), 0
n = list(map(int, input().split()))  # numbers
w = list(map(int, input().split()))  # weight

for i in range(x): s += n[i] * w[i]
print(round(s/sum(w),1))

# Alternative for 2 last row of code:
# print("%.1f" % (sum(list(map(lambda x : x[0] * x[1], zip(n,w)))) / sum(w)))