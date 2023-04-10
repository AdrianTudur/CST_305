import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



start_time = time.time()

print("the total run time is --- %s seconds ---" % (time.time() - start_time))

# Define equation for part 1(a)
def part1a(x):
    # Create Taylor series based on work done by hand
    y0 = 1  # initial value
    y1 = -x  # initial value for y' over factorial 1
    y2 = (0 / 2) * pow(x, 2)   # initial value for y'' over factorial 2
    y3 = (-2 / 6) * pow(x, 3)    # initial value for y''' over factorial 3
    y4 = (-2 / 24) * pow(x, 4)   # initial value for y'''' over factorial 4
    return y0 + y1 + y2 + y3 + y4


# Define equation for part 1(b)
def part1b(x):
    # Create Taylor series based on work done by hand
    y0 = 6  # initial value
    y1 = x - 3 # initial y' over factorial 1
    y2 = (11 / 2) * pow((x-3),2) # initial y'' over factorial 2
    return y0 + y1 + y2


# Define equations for part 2
def part2(x, a0, a1):   # split solution into halves a0 and a1
    a = a0 + (a1 * x) - (a0 * pow(x, 2) / 8) - (a1 * pow(x, 3) / 24) + (a0 * pow(x, 4) / 128) + (7 * a1 * pow(x, 5) / 1920) - (13 * a0 * pow(x, 6) / 15360) - (7 * a0 * pow(x, 7) / 15360) + (403 * a0 * pow(x, 8) / 3440640) + (301 * a1 * pow(x, 9) / 4423680) - (7657 * a0 * pow(x, 10) / 412876800)
    return a 


n = 100000   # number of steps
dt = 0.02   # step size
xs = np.linspace(1,10, n)   # create x-space array
ysa = np.empty(n)   # y-space for part 1(a)
ysb = np.empty(n)   # y-space for part 1(b)
ys2 = np.empty(n)   # y-space for part 2

for i in range(-n, n):
    ysa[i] = part1a(i * dt)
    ysb[i] = part1b(i * dt)
    ys2[i] = part2(i * dt, 2, 2)

# Graph part 1(a)
plt.title("Part 1(a)")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(xs, ysa)
plt.show()

# Graph part 1(b)
plt.title("Part 1(b)")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(xs, ysb)
plt.show()

# Graph part 2
plt.title("Part 2")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(xs, ys2)
plt.show()
