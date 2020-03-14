from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

ydata = [3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07,
         15.51, 16.92, 18.31, 19.68, 21.03, 22.36, 23.68, 25]
xdata = [i for i in range(1, 16)]


def linear(x, a, b):
    return a*x + b


def sqrt(x, a, b):
    return a * np.sqrt(x) + b


def log(x, a, b):
    return a * np.log(x) + b


def quad(x, a, b, c):
    return a*x ** 2 + b * x + c


def quad2(x, a, b):
    return a * x ** 2 + b


func = quad
l = curve_fit(func,  xdata, ydata)[0]
x = np.linspace(1, 15)
y = [func(i, *l) for i in x]
n = [round(x, 2) for x in l]
# s = "$ {0} \\sqrt {{ x }} + {1}$".format(*n)
# s = "$ {0} x + {1} $".format(*n)
s = "$ {0} x^2 + {1} x + {2}$".format(*n)

plt.scatter(xdata, ydata)
plt.plot(x, y, label=s)
plt.legend(loc='upper right')
plt.show()
