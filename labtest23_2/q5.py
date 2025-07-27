from numpy import array, zeros, ones, identity, diag, linspace,inf, sqrt, exp, pi, sin, cos, log
from numpy.linalg import norm, eigvals, cond, lstsq, solve
from matplotlib.pyplot import plot, show
from scipy.linalg import lu, qr
from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve

def approx(N):
    h = 1/N
    x = linspace(0, 1, N + 1)
    d1 = (-2 - h**2) * ones(N)
    d2 = ones(N-1)

    A = diag(d1) + diag(d2, 1) + diag(d2, -1)
    a0 = zeros(N)
    a0[0] = 3
    a0[1] = -4
    a0[2] = 1
    A[0] = a0

    a = ones(N) * h**2 * (1 + pi**2 / 4) * cos(pi + pi * x[:N] / 2)
    a[0] = 0
    return solve(A, a)

print(approx(4))

E = zeros(3)
for i in range(0, 3):
    N = 2 ** i * 80
    x = linspace(0, 1, N + 1)
    E[i] = norm(approx(N) - cos(pi/2*x[:N]).T, inf)

OC = zeros(2)
OC[0] = log(E[0] / E[1]) / log(2)
OC[1] = log(E[1] / E[2]) / log(2)
print(E)
print(OC)
