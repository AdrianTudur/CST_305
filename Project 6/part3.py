import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from datetime import datetime

start = datetime.now()

def func(y, p, k):
    dydp = (k / (p*8))
    return dydp

y0 = 0
p = np.linspace(100, 1600)


k = 3000000000
y1 = odeint(func, y0, p, args=(k,))
k = 2000000000
y2 = odeint(func, y0, p, args=(k,))
k = 1000000000
y3 = odeint(func, y0, p, args=(k,))
k = 500000000
y4 = odeint(func, y0, p, args=(k,))
k = 250000000
y5 = odeint(func, y0, p, args=(k,))
k = 125000000
y6 = odeint(func, y0, p, args=(k,))

end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution is : {td:.03f}ms")

f = plt.figure()
f.set_figwidth(12)
f.set_figheight(4)
plt.plot(p, y1, 'r-', linewidth=2, label='3 GB')
plt.plot(p, y2, 'b-', linewidth=2, label='2 GB')
plt.plot(p, y3, 'g-', linewidth=2, label='1 GB')
plt.plot(p, y4, 'k-', linewidth=2, label='0.5 GB')
plt.plot(p, y5, 'y-', linewidth=2, label='0.25 GB')
plt.plot(p, y6, 'm-', linewidth=2, label='0.125 GB')
plt.title('Speed of Ethernet')
plt.xlabel('Frame Size')
plt.ylabel('Frame Rate')
plt.legend()
plt.show()