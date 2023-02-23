import math


y0 = 1
x0 = 2
steps = 6
e = 2.71828183


def f(x, y):
    return (-y)+(math.log(x))


def rk4(x0, y0, n):
    h = 0.03

    print('---------------SOLUTION----------------')
    print('  n      x0       y0     True Solution      ')
    print('---------------------------------------')
    for i in range(n):
        k1 = (f(x0, y0))
        k2 = (f((x0 + (h/2)), (y0 + (h / 2) * k1)))
        k3 = (f((x0 + h / 2), (y0 + (h / 2) * k2)))
        k4 = (f((x0 + h), (y0 + h * k3)))
        k = (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        yn = y0 + k
        print('  %.0f\t%.4f\t%.4f     %.4f' % (i ,x0, y0, yn))
        print('---------------------------------------')
        y0 = yn
        x0 = x0 + h

rk4(x0, y0, steps)