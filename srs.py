import math
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.pyplot import figure

# Spaced Repetition System (SRS) based on Hermann Ebbinghaus' theory of the forgetting curve

Ak = 1.48
Ac = 1.25

def dgen(k, c):
    def f(t):
        return k / (math.log(t)**c + k)

    return f


def linear_srs(days):
    Rs = [[(0, 1)]] # Retention rates
    funcs = [dgen(Ak, Ac)]

    for day in range(1, days + 1):
        Rs_len = len(Rs)
        for i in range(0, Rs_len):
            Rs[i].append((day, funcs[i](day - i + 1)))

        Rs.append([(day, 1)])
        new_k = 1 / (1 - Rs[-2][1][1])
        funcs.append(dgen(new_k, Ac))

    return Rs

def growing_srs(days, ease=2.5, ideal_retention=.8):
    Rs = [[(1.0, 1.0)]] # Retention rates
    funcs = [dgen(Ak, Ac)]

    i = 0
    while i < len(Rs):
        reviewed = False
        first_day = Rs[i][0][0]

        # Calculate retention rate for each day
        for day in range(int(first_day) + 1, days):
            retention = funcs[i](day - first_day + 1)
            Rs[i].append((day, retention))

            # Create new forgetting curve when reviewing
            if (not reviewed and retention < ideal_retention):
                Rs.append([(day, 1)])
                new_k = 1. / (1. - Rs[i][1][1])
                funcs.append(dgen(new_k, Ac))
                reviewed = True
        i += 1
    return Rs


def plot_figure(axs, title, vals):
    axs.set_title(title)
    for i in range(0, len(vals)):
        axs.plot(*zip(*vals[i]))

fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(7, 9))

plot_figure(axs[0], "Growing SRS", growing_srs(14))
plot_figure(axs[1], "Linear SRS", linear_srs(14))

plt.show()
