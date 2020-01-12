import matplotlib.pyplot as plt
import math

width  = input("width:") # mm
length = input("length:") # mm

def volume_of_box(width, length, height):
    return (width - height * 2) * (length - height * 2) * height

cx = []
cy = []
# cw = []
# cl = []

highest = 0
high_i = 0;

for i in range(1, min(width, length) / 2):
    ht = volume_of_box(width, length, i)

    if ht > highest:
        highest = ht
        high_i = i

    # cw.append(width - i * 2)
    # cl.append(length - i * 2)
    cx.append(i)
    cy.append(ht**(1. / 3))

print("Largest box was", highest**(1./3), "mm^3 with a height of", high_i, "mm")

plt.plot(cx, cx)
# plt.plot(cx, cw)
# plt.plot(cx, cl)
plt.plot(cx, cy)
plt.ylabel("volume (mm^3)")
plt.xlabel("height (mm)")
plt.grid(True)
plt.show()
