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
        x = (2*x) % 1
        y = y/2
    else:
        x = 2*x % 1
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
def countLabels(i,statelabels):
    bernoulliCount = {"A": 0,"B": 0}
    for j in set(statelabels):
        bernoulliCount[j] = statelabels.count(j)
    proportionA = bernoulliCount["A"]/i
    return [bernoulliCount,proportionA]


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
    dict["X"].append(statesx[i])
    dict["Y"].append(statesy[i])
    dict["Label"].append(statelabels[i])
    if statesx[i] <=0.5 and statesy[i] <=0.5:
        ax.plot(dict["X"][i], dict["Y"][i], "bo", markersize= 10)
        plt.text(dict["X"][i], dict["Y"][i], str(i+1), ha='center', va="center_baseline", size=9, color='white', weight="heavy")


    elif statesx[i] >= 0.5 >= statesy[i]:
        ax.plot(dict["X"][i], dict["Y"][i], "ro", markersize= 10)
        plt.text(dict["X"][i], dict["Y"][i], str(i + 1), ha='center', va="center_baseline", size=9, color='white', weight="heavy")

    elif statesx[i] <= 0.5 <= statesy[i]:
        ax.plot(dict["X"][i], dict["Y"][i], "ro", markersize= 10)
        plt.text(dict["X"][i], dict["Y"][i], str(i + 1), ha='center', va="center_baseline", size=9, color='white', weight="heavy")

    else:
        ax.plot(dict["X"][i], dict["Y"][i], "bo", markersize= 10)
        plt.text(dict["X"][i], dict["Y"][i], str(i + 1), ha='center', va="center_baseline", size=9, color='white', weight="heavy")

    # convoluted formatting
    if countLabels(i+1,dict["Label"])[0]["A"] == 0:
        a = "%02d" % 0
    else:
        a = ["%02d" % x for x in range(countLabels(i+1,dict["Label"])[0]["A"]+1)][-1]
    if countLabels(i + 1, dict["Label"])[0]["B"] == 0:
        b = "%02d" % 0
    else:
        b = ["%02d" % x for x in range(countLabels(i+1,dict["Label"])[0]["B"]+1)][-1]
    c = "%.2f" % round(countLabels(i+1,dict["Label"])[1],2)
    d = "%.2f" % float(1-float(c))
    plt.figtext(0.5, 0.95, f"A: {a} B: {b} A%: {c} B%: {d}", ha="center", va="center", fontsize=18, bbox={"facecolor": "white"})
    for txt in fig.texts[:-1]:
        txt.set_visible(False)

# fixes the double 0 index problem,
# the double 0 comes from an initialization of the animation,
# now the initialization is to do nothing
def doNothing():
    pass

ani = FuncAnimation(fig, animate,frames=n, init_func=doNothing,interval=250, repeat=False)

plt.show()
