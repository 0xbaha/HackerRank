# Simple way
After drawing the first red marble, we are left with 2 red marbles and 4 blue marbles, so the probability of drawing a second blue marble is: 4 / 6 = `2/3`

# Complex way
## events:
FR = first red marble
FB = first blue marble
SR = second red marble
SB = second blue marble

## outcomes in experiment:
total number of outcomes: 2P7 = 7! / (7-2)! = 7 * 6 = 42 # Permutation
number of outcomes in event (FR and SB): 3 * 4 = 12

## probability:
P(FR) = 3/7
P(FR and SB) = 12 / 42 = 2/7 # Classical definition of probability

P(SB | FR) = P(SB and FR) / P(FR) # Conditional Probability
= P(FR and SB) / P(FR)
= 2/7 / 3/7
= `2/3`