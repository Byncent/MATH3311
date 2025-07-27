from numpy import ones, sqrt, pi, sin, linspace, zeros
from scipy.special import gamma

N = 9
h = 1/N
x = linspace(0, 1, N+1)
w = 2 * ones(N+1)
w[1] = 1
w[-1] = 1
f = (2 - 2 * x)** 1.5 * sqrt(x)
trapf = h/2 * w @ f.T

tsol = 16/(15 * pi ** 0.5) * (gamma(0.75)) ** 2
errtrap = abs(tsol - trapf)


N = 9
h = 1/N
x = linspace(0, 1, N+1)
y = linspace(0, 1, N+1)
F = zeros((N+1, N+1))
for i in range(N+1):
    for j in range(N+1):
        F[i][j] = sin(x[i] * y[j]) * sqrt(x[i] + 2 * y[j])

trap2dF = (h**2 / 4) * w @ F @ w.T
print(f"trapfF = {trap2dF}")