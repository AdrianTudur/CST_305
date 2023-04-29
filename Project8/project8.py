# import libraries and packages needed for project
from scipy import pi
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()

def reimann_plot_part1(f, minlim, maxlim, N, title, xaxis, yaxis):

    # Define step sizes and range for each part
    n = 1000
    x = np.linspace(minlim, maxlim, N + 1)
    y = f(x)
    X = np.linspace(minlim, maxlim, n * N + 1)
    Y = f(X)
    theta = np.arange(-pi, pi+pi/2, step=(pi / 2))

    # Define all pieces of the plots needed
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.plot(X, Y, 'b')
    x_left = x[:-1]
    y_left = y[:-1]
    plt.plot(x_left, y_left, 'b.', markersize=10)
    plt.bar(x_left, y_left, width=(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Left Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.xticks(theta, ['π', '-π/2', '0', 'π/2', 'π'])
    plt.subplot(1, 3, 2)
    plt.plot(X, Y, 'b')
    x_mid = (x[:-1] + x[1:]) / 2
    y_mid = f(x_mid)
    plt.plot(x_mid, y_mid, 'b.', markersize=10)
    plt.bar(x_mid,y_mid, width = (maxlim - minlim) / N, alpha=0.2, edgecolor='b')
    plt.title('Midpoint Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.xticks(theta, ['π', '-π/2', '0', 'π/2', 'π'])
    plt.subplot(1, 3, 3)
    plt.plot(X, Y, 'b')
    x_right = x[1:]
    y_right = y[1:]
    plt.plot(x_right, y_right, 'b.', markersize=10)
    plt.bar(x_right, y_right, width=-(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Right Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.xticks(theta, ['π', '-π/2', '0', 'π/2', 'π'])
    plt.suptitle(title, fontsize=16, fontweight="bold")
    plt.show()


def reimann_plot(f, minlim, maxlim, N, title, xaxis, yaxis):

    # Define step sizes and range for each part
    n = 1000
    x = np.linspace(minlim, maxlim, N + 1)
    y = f(x)
    X = np.linspace(minlim, maxlim, n * N + 1)
    Y = f(X)

    # Define all pieces of the plots needed
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.plot(X, Y, 'b')
    x_left = x[:-1]
    y_left = y[:-1]
    plt.plot(x_left, y_left, 'b.', markersize=10)
    plt.bar(x_left, y_left, width=(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Left Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.subplot(1, 3, 2)
    plt.plot(X, Y, 'b')
    x_mid = (x[:-1] + x[1:]) / 2
    y_mid = f(x_mid)
    plt.plot(x_mid, y_mid, 'b.', markersize=10)
    plt.bar(x_mid,y_mid, width = (maxlim - minlim) / N, alpha=0.2, edgecolor='b')
    plt.title('Midpoint Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.subplot(1, 3, 3)
    plt.plot(X, Y, 'b')
    x_right = x[1:]
    y_right = y[1:]
    plt.plot(x_right, y_right, 'b.', markersize=10)
    plt.bar(x_right, y_right, width=-(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Right Riemann Sum, N = {}'.format(N))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.suptitle(title, fontsize=16, fontweight="bold")
    plt.show()

def reimann_sum(f, minlim, maxlim, N, ):

    # Calculate the width of each subinterval
    dx = (maxlim - minlim)/N

    # Generate array of midpoint, left, and right endpoints of subintervals
    x_left = np.linspace(minlim, maxlim - dx, N)
    x_midpoint = np.linspace(minlim + dx / 2, maxlim - dx / 2, N)
    x_right = np.linspace(minlim + dx, maxlim, N)

    # Calculate left, right, and mid Riemann sum using given function and endpoints
    left_riemann_sum = np.sum(f(x_left) * dx)
    print("Left Riemann Sum:\t", left_riemann_sum)
    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
    print("Midpoint Riemann Sum:\t", midpoint_riemann_sum)
    right_riemann_sum = np.sum(f(x_right) * dx)
    print("Right Riemann Sum:\t", right_riemann_sum)


# Define functions for all parts of the project
a = lambda x: np.sin(x) + 1
b = lambda x: (3 * x) + (2 * (x ** 2))
c1 = lambda x: np.log(x)
c2 = lambda x: (x ** 2) - (x ** 3)
p2 = lambda x: -0.0004 * x ** 4 + 0.026 * x ** 3 - 0.516 * x ** 2 + 3.135 * x + 19.55

# Print calculated values for left, right, and mid riemman sums and true vales for each problem
print("\nThe Riemman Sum of the function in Part 1a is:"); reimann_sum(a, -pi, pi, 4)
print("The correct value for part 1a is: ", quad(a, -pi, pi)[0])
print("\nThe Riemman Sum of the function in Part 1b is:"); reimann_sum(b, 0, 1, 1000)
print("The correct value for part 1b is: ", quad(b, 0, 1)[0])
print("\nThe Riemman Sum of the function in Part 1c1 is:"); reimann_sum(c1, 1, np.e, 1000)
print("The correct value for part 1c1 is: ", quad(c1, 1, np.e)[0])
print("\nThe Riemman Sum of the function in Part 1c2 is:"); reimann_sum(c2, -1, 0, 1000)
print("The correct value for part 1c2 is: ", quad(c2, -1, 0)[0])
print("\nThe Riemman Sum of the function in Part 2 is:"); reimann_sum(p2, 0, 30, 1000)
print("The correct value for part 2 is: ", quad(p2, 0, 30)[0])


# Plot the graphs for each part
reimann_plot_part1(a, -pi, pi, 4, "Part 1.a", "x-axis", "y-axis")
reimann_plot(b, 0, 1, 50, "Part 1.b", "x-axis", "y-axis")
reimann_plot(c1, 1, np.e, 50, "Part 1.c1", "x-axis", "y-axis")
reimann_plot(c2, -1, 0, 50, "Part 1.c2", "x-axis", "y-axis")
reimann_plot(p2, 0, 30, 50, "Part 2", "Time (min)", "Mbps")

