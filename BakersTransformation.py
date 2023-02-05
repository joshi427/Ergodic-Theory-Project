import numpy as np
import matplotlib.pyplot as plt
from random import randint
from matplotlib.animation import FuncAnimation

# starting state
start = [0.26,0.33]

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

# counts frequency of A and B
bernoulliCount = {}
for i in set(statelabels):
    bernoulliCount[i] = statelabels.count(i)
proportionA = bernoulliCount["A"]/n
proportionB = bernoulliCount["B"]/n
print(f"Proportion of A's: {proportionA} \nProportion of B's: {proportionB}")
print(states)

# plot animation
x = []
y = []
fig, ax = plt.subplots()

# Bernoulli regions
ax.hlines(y=0.5, xmin=0, xmax=1)
ax.vlines(x=0.5, ymin=0, ymax=1)
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.fill_between([0,0.5], 0, 0.5, color='blue', alpha=.2)
ax.fill_between([0.5,1], 0, 0.5, color='red', alpha=.2)
ax.fill_between([0.5,1], 0.5, 1, color='blue', alpha=.2)
ax.fill_between([0,0.5], 0.5, 1, color='red', alpha=.2)
def animate(i):
    x.append(statesx[i])
    y.append(statesy[i])
    ax.plot(x, y, "bo")

ani = FuncAnimation(fig, animate, frames=n, interval=250, repeat=False)

plt.show()