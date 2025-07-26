from numpy import array, zeros, ones, identity, exp, linspace, sin, cos, pi
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu
from scipy.interpolate import CubicSpline
from scipy.fft import fft

tdat = array([i for i in range(10)])
ydat = array([106.236, 183.683, 139.279, 160.48, 207.895, 463.666, 388.06, 407.674, 442.974, 509.423])

teval = linspace(1.5, 9.5, 9)
spline = CubicSpline(tdat, ydat)
yspteval = spline(teval)

w = fft(ydat)
rw = w.real
iw = w.imag

m = 10
p = 5
a0 = w[0]/m

a = 2 * rw[1:6]/m
a[4] = w[5]/m

b = -2 * iw[1:6]/m
b[4] = 0

yteval = a0
for k in range(1, p+1):
    yteval = yteval + a[k-1] * cos(2 * pi * k / m * teval) + b[k-1] * sin(2 * pi * k / m * teval)

print(yteval)
