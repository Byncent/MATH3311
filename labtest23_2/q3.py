from numpy import array, zeros, ones, identity, diag, linspace, sqrt, exp
from numpy.linalg import norm, eigvals, cond, lstsq
from matplotlib.pyplot import plot, show
from scipy.linalg import lu, qr
from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve

def f(x):
    return 40 * x ** 2 + 1 / (1+x) ** 3 - 4 * exp(2 * x)
def df(x):
    return 80 * x - 3 / (1+x) ** 4 - 8 * exp(2 * x)

xs = linspace(0, 2, 1000)

plot(xs, f(xs))
show()
nfzero = 2

xfzero = fsolve(f, 1/4)
print(xfzero)

xa = 0
xb = 1/4

while abs(xa - xb) > 10**(-15):
    xnew = xb - f(xb)/df(xb)
    xa = xb
    xb = xnew

print(xb)

xxs = zeros(4)
Error = zeros(3)
xxs[0] = 1/4
for i in range(1, 4):
    xxs[i] = xxs[i-1] - f(xxs[i-1])/df(xxs[i-1])
    Error[i - 1] = xxs[i] - xfzero

print(Error)

xsecs = zeros(6)
xsecs[1] = 1
for i in range(2, 6):
    xsecs[i] = xsecs[i-1] - f(xsecs[i-1])/(f(xsecs[i-1]) - f(xsecs[i-2])) * (xsecs[i-1] - xsecs[i-2])

xs5 = xsecs[5]
print(xs5)