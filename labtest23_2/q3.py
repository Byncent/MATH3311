from numpy import array, zeros, ones, identity, diag, linspace, sqrt, exp
from numpy.linalg import norm, eigvals, cond, lstsq
from matplotlib.pyplot import plot
from scipy.linalg import lu, qr
from scipy.interpolate import CubicSpline

def f(x):
    return 40 * x ** 2 + 1 / (1+x) ** 3 - 4 * exp(2 * x)

xs = linspace(0, 2, 1000)

plot(xs, f(xs))

