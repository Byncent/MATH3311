from numpy import array, zeros, ones, identity, exp, linspace, sin, pi
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu

N = 6
h = 1/N
x = linspace(0, 1, N+1)
w = 2 * ones(N+1)
w[0] = 1
w[N] = 1

f = 3**x * sin(pi * x) ** 2
Qf = h * w @ f / 2
print(Qf)

ws = 4 * ones(N+1)
ws[::2] = 2
ws[0] = 1
ws[-1] = 1
Qfs = h/3 * ws @ f
print(Qfs)