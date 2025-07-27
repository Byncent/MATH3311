from numpy import  ones, linspace, loadtxt, pi, exp, cos, sin, array, vander, zeros
from scipy.interpolate import  CubicSpline
from scipy.fft import fft 
from scipy.linalg import lstsq
import numpy as np

tdata = linspace(1, 10, 10)
ydata = array([77.64, 94.53, 68.17, 39.68, 56.99, 65.23, 50.8, 43.29, 48.66, 93.17])

pp = CubicSpline(tdata, ydata)
teval = linspace(1.3, 9.3, 9)
yspteval = pp(teval)
print(yspteval)

A = ones([10, 4])
A[:, 1] = tdata
A[:, 2] = exp(tdata)
A[:, 3] = cos(pi * tdata / 2)
xLs = lstsq(A, ydata)[0]
print(f"xLs = {xLs}")

yLSteval = xLs[0] + xLs[1] * teval + xLs[2] * exp(teval) + xLs[3] * cos(pi * teval/2)
print(f"yLSteval = {yLSteval}")



m = 10
w = fft(ydata)
a0 = w[0].real/m
a = zeros(5)
for i in range(1, 5):
    a[i-1] = 2/m * w[i].real
a[4] = w[5].real/m
print(f"a = {a}")

b = array([3.9119, 1.7992, -0.4331, -4.9655, 0])
ydfteval = a0
for i in range(5):
    ydfteval += a[i] * cos(2 * pi * (i + 1) * teval / m) + b[i] * sin(2 * pi * (i + 1) * teval / m)

print(f"ydfteval = {ydfteval}")