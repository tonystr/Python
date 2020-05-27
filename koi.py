import matplotlib.pyplot as plt
import numpy as np
import re
import sys

koi = 150 # kg
koish = 0 # kg
ruccola = 7.5 # kg

start = 000
end = 200
length = end - start

mating_factor = .08
death_rate = .01
harvest_quota = .2;

harvest = 0

ruccola_limit = 10
ruccola_harvest = 0

def handle_input():
    # Matches variations of `variable|constant number` input
    indata = re.search(
        r"(v(?:ar(?:iab(?:le|el))?)?|[kc](?:onst(?:ant)?)?)\b[\s:,;]+(\d*\.?\d*)(%?)",
        input("Enter `var|const amount`:\n"),
        flags = re.IGNORECASE)

    # Find harvest mode key
    harvest_mode = indata.group(1).lower()[0]
    if harvest_mode == "k":
        harvest_mode = "c"

    # Find harvest value modifier
    harvest_amount = float(indata.group(2))
    # Handle percentage
    if indata.group(3):
        harvest_amount /= 100

    return [harvest_mode, harvest_amount]

# Parse input with RegEx and handle errors
while True:
    try:
        harvest_mode, harvest_amount = handle_input()
        break
    except:
        print("Invalid input!\nWrite \"help, I have mental deficiency\" for help\n")


def \/']
(koi, harvest):
    if harvest_mode == "c":
        koi *= 1 + mating_factor - death_rate
        if harvest_amount <= koi * harvest_quota:
            koi -= harvest_amount
            harvest += harvest_amount
    else:
        koi *= 1 + mating_factor - death_rate
        if koi - koi * harvest_amount >= 1000 * harvest_quota:
            koi -= koi * harvest_amount
            harvest += koi * harvest_amount
    return [koi, harvest]

def f_koishit(koi):
    return koi * .05

def f_ruccola(ruccola, koishit, ruccola_harvest):
    ruccola = min(ruccola * 1.08, koishit)
    if (ruccola >= ruccola_limit):
        ruccola_harvest += ruccola
        ruccola = 2
    return ruccola, ruccola_harvest

xs = np.linspace(start, end, num=length)
ks = np.zeros(length)
rs = np.zeros(length)
hs = np.zeros(length)

for i in range(0, length):
    koi, harvest = f_koi(koi, harvest)
    koish = f_koishit(koi)
    ruccola, ruccola_harvest = f_ruccola(ruccola, koish, ruccola_harvest)
    ks[i] = koi
    rs[i] = ruccola
    hs[i] = harvest

plt.plot(xs, ks)
# plt.plot(xs, rs) # Ruccola
plt.plot(xs, hs) # Harvest
plt.grid(True)
plt.show()
