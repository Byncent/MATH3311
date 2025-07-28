from numpy import ones, linspace, loadtxt, pi, sqrt, cos, sin, array, ones
from scipy.interpolate import CubicSpline
from scipy.fft import fft
from scipy.linalg import lstsq

tdata = linspace(1, 9, 9)
ydata = array([94.88, 79.48, 61.95, 99.67, 72.34, 66.05, 56.64, 41.51, 31.08])

teval = linspace(0.5, 9.5, 10)
pp = CubicSpline(tdata, ydata)
yspteval = pp(teval)

A = ones((9, 5))
A[:, 1] = tdata
A[:, 2] = tdata ** 2
A[:, 3] = sqrt(tdata)
A[:, 4] = sin(pi * tdata / 2)

xLs = lstsq(A, ydata)[0]
print(f"xLs = {xLs}")

yLSteval = xLs[0] + xLs[1] * teval + xLs[2] * teval ** 2 + xLs[3] * sqrt(teval) + xLs[4] * sin(pi * teval / 2)
print(f"yLSteval = {yLSteval}")


w = fft(ydata)
m = 9
a0 = w[0].real/m
print(f"a0 = {a0}")

b = -2 * w[1:5].imag/m
print(f"b = {b}")

a = [-2.3688, 9.9369, 16.6633, 3.5819]
ydfteval = a0
for i in range(4):
    ydfteval += a[i] * cos(2 * pi * (i + 1) * teval / m) + b[i] * sin(2 * pi * (i + 1) * teval / m)

print(f"yddfteval = {ydfteval}")
