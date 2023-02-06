import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import math

start = time.time()

ya = []
xa = []
y0 = 1
x0 = 2
steps = 10000


def f(x, y):
    return (-y)+(math.log(x))

def model(y, x):
    return (-y)+(math.log(x))


axs = plt.subplots(3, sharex=True, sharey=True)

def rk4(x0, y0, n):
    h = 0.03

    for i in range(n):
        k1 = (f(x0, y0))
        k2 = (f((x0 + (h/2)), (y0 + (h / 2) * k1)))
        k3 = (f((x0 + h / 2), (y0 + (h / 2) * k2)))
        k4 = (f((x0 + h), (y0 + h * k3)))
        k = (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        yn = y0 + k
        y0 = yn
        x0 = x0 + h

        ya.append(y0)
        xa.append(x0)  
    plt.subplot(311)      
    plt.plot(xa, ya, 'y-', linewidth=4, label='Rk4')
    plt.legend()

    plt.subplot(313)    
    plt.plot(xa, ya, 'y-', linewidth=4, label='Rk4')
    plt.legend()

rk4(x0, y0, steps)

x = np.linspace(2, 300, steps)

y = odeint(model, y0, x)

plt.subplot(312)
plt.plot(x, y, label='ODEINT')
plt.legend()

plt.subplot(313)
plt.plot(x, y, label='ODEINT')
plt.legend()
plt.show()

end = time.time()


print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")