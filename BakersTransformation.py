import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import pandas as pd

# starting state
start = [random.uniform(0,1),random.uniform(0,1)]

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
# plt.scatter(statesx,statesy)
# plt.show()

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
dict = {"X": [], "Y": [], "Label": []}
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
ax.annotate("A",xy=(0.25,0.25), ha = "center", va = "center", size = 20, color = "blue")
ax.annotate("A",xy=(0.75,0.75), ha = "center", va = "center", size = 20, color = "blue")
ax.annotate("B",xy=(0.25,0.75), ha = "center", va = "center", size = 20, color = "red")
ax.annotate("B",xy=(0.75,0.25), ha = "center", va = "center", size = 20, color = "red")

def animate(i):
    i = i+1
    print(i)
    dict["X"].append(statesx[i])
    dict["Y"].append(statesy[i])

    if statesx[i] <=0.5 and statesy[i] <=0.5:
        ax.plot(dict["X"][i], dict["Y"][i], "bo")
    elif statesx[i] >= 0.5 >= statesy[i]:
        ax.plot(dict["X"][i], dict["Y"][i], "ro")
    elif statesx[i] <= 0.5 <= statesy[i]:
        ax.plot(dict["X"][i], dict["Y"][i], "ro")
    else:
        ax.plot(dict["X"][i], dict["Y"][i], "bo")

ani = FuncAnimation(fig, animate, frames=n, interval=250, repeat=False)

plt.show()

print("dict")
print(dict["X"])
print("states")
print(states)
print(statesx)
print(statesy)