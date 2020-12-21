#!/bin/python3

a,b = 1,3
ins = 5
prob_defect = a/b
prob_good = 1-prob_defect
prob = 0
for i in range(ins):
    prob+=(prob_good**i)*prob_defect
print('{:.3f}'.format(prob))