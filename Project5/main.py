import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, r, s=10, b=(8/3)):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

xs[0], ys[0], zs[0] = (11.8, 4.4, 2.4)


j = 0
while j <= 3:
    rval = int(input("Enter a value for r: "))
    j=j+1
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], rval)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()

    plt.plot(xs)
    plt.xlabel("t")
    plt.ylabel("x - JPG")
    plt.title("x(t) [JPG] - r: " + str(rval))
    plt.show()

    plt.plot(ys)
    plt.xlabel("t")
    plt.ylabel("y - PNG")
    plt.title("y(t) [PNG] - r: " + str(rval))
    plt.show()

    plt.plot(zs)
    plt.xlabel("t")
    plt.ylabel("z - GIF")
    plt.title("z(t) [GIF] - r: " + str(rval))
    plt.show()
