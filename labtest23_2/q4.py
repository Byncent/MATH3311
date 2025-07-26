from numpy import array, zeros, ones, identity, diag, linspace, sqrt, exp, pi, sin, cos, log
from numpy.linalg import norm, eigvals, cond, lstsq
from matplotlib.pyplot import plot, show
from scipy.linalg import lu, qr
from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve

def approx(N):
    h = pi/(2*N)
    x = linspace(0, pi/2, N+1)
    w = 2 * ones(N+1)
    w[0] = 1
    w[-1] = 1

    f = cos(3 * x)/ (sin(x) + 1)
    Qf = h/2 * w @ f.T

    ws = 4 * ones(N+1)
    ws[::2] = 2
    ws[0] = 1
    ws[-1] = 1
    Qfs =  h/3 * ws @ f.T
    trueSol = 2 - log(8)
    print(abs(Qf - trueSol))
    print(abs(Qfs - trueSol))

approx(100)

from numpy import cos, log, ones, pi, sin, linspace

# Coarse grid (N = 6)
N = 6
h = pi / 2 / N
x = linspace(0, pi / 2, N + 1)
f = cos(3 * x) / (sin(x) + 1)

# Trapezoidal rule
w = 2 * ones(N + 1)
w[0] = 1
w[N] = 1
Qf = h / 2 * w @ f.T

# Simpson’s rule
ws = 2 * ones(N + 1)
ws[0] = 1
ws[N] = 1
ws[1::2] = 4
Qfs = h / 3 * ws @ f.T

# Fine grid (N1 = 100)
N1 = 100
h1 = pi / 2 / N1
x1 = linspace(0, pi / 2, N1 + 1)
f1 = cos(3 * x1) / (sin(x1) + 1)

# Trapezoidal rule on fine grid
w1 = 2 * ones(N1 + 1)
w1[0] = 1
w1[N1] = 1
Qf1 = h1 / 2 * w1 @ f1.T
# Simpson's rule on fine grid
w1[1::2] = 4
Qfs1 = h1 / 3 * w1 @ f1.T

# Exact value of integral
trsol = 2 - log(8)

# Errors
errtrap = abs(Qf1 - trsol)
errsimp = abs(Qfs1 - trsol)
print(errtrap)
print(errsimp)