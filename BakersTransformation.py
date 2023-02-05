import numpy as np
import matplotlib.pyplot as plt

# starting state
start = [0.2333,0.222]

# time
n = 50

# Baker's transform
def transform(x,y):
    if x <= 0.5:
        x = 2*x
        y = y/2
    else:
        x = 2*x - 1
        y = y/2 + 0.5
    return [x,y]

# n transformations
i = 0
states = [start for j in range(n)]
while i < n -1:
    states[i+1] = transform(states[i][0],states[i][1])
    i += 1

statesx = [0 for j in range(n)]
statesy = [0 for j in range(n)]
for i in range(n):
    statesx[i] = states[i][0]
    statesy[i] = states[i][1]

# plot transformations
plt.scatter(statesx,statesy)
plt.show()

# dividing space into A and B
statelabels = [0 for j in range(n)]
for i in range(n):
    if statesx[i] <=0.5 and statesy[i] <=0.5:
        statelabels[i] = "A"
    elif statesx[i] >=0.5 and statesy[i] <=0.5:
        statelabels[i] = "B"
    elif statesx[i] <=0.5 and statesy[i] >=0.5:
        statelabels[i] = "A"
    else:
        statelabels[i] = "B"

print(statelabels)
duplicateFrequencies = {}
for i in set(statelabels):
    duplicateFrequencies[i] = statelabels.count(i)

print(duplicateFrequencies)