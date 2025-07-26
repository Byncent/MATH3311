from numpy import array, zeros, ones, identity, diag, linspace, sqrt, exp, pi, sin, cos, log
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
    A[0] = [3, -4, 1, 0]

    a = ones(N) * h**2 * (1 + pi**2 / 4) * cos(pi + pi * x[:N] / 2)
    a[0] = 0
    print(a)
    U4 = solve(A, a)


# Initial parameters
N = 4
x = linspace(0, 1, N + 1)
U4 = zeros(N)
h = 1 / N

# Matrix components
d1 = ones(N - 1)
d4 = ones(N - 1)
d1[0] = -4

d2 = zeros(N - 2)
d2[0] = 1

d3 = ones(N) * (-2 - h**2)
d3[0] = 3

# Construct matrix A and right-hand side vector a
A = diag(d1, 1) + diag(d4, -1) + diag(d3) + diag(d2, 2)
a = zeros(N)
a[1:] = h**2 * (1 + pi**2 / 4) * cos(pi + pi / 2 * x[1:N])
print(a)
# Solve system
U4 = solve(A, a)


approx(4)