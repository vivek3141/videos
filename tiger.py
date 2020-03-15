from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

ydata = [3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07,
         15.51, 16.92, 18.31, 19.68, 21.03, 22.36, 23.68, 25,
         26.3, 27.59, 28.87, 30.14, 31.41, 33.92, 36.42, 38.89, 41.34,
         43.77, 46.19, 48.6, 53.38, 58.12, 62.83, 67.5]
print(len(ydata))
xdata = [i for i in [*range(1, 21), *range(22, 33, 2), *range(38, 51, 4)]]
print(len(xdata))


def linear(x, a, b):
    return a*x + b


def sqrt(x, a, b):
    return a * np.sqrt(x) + b


def log(x, a, b):
    return a * np.log(x) + b


def quad(x, a, b, c):
    return a*x ** 2 + b * x + c


def exp(x, a, b, c):
    return a*x ** b + c


func = sqrt
l = curve_fit(func,  xdata, ydata)[0]


def f(x): return func(x, *l)


x = np.linspace(1, 50)
y = [f(i) for i in x]
n = [round(a, 2) for a in l]
s = "$ {0} \\sqrt {{ x }} + {1}$".format(*n)
#s = "$ {0} x + {1} $".format(*n)
#s = "$ {0} x^2 + {1} x + {2} $".format(*n)
#s = "$ {0} e^x + {1} $".format(*n)

plt.scatter(xdata, ydata)
plt.plot(x, y, label=s)
plt.legend(loc='upper right')
plt.show()
