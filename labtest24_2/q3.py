from numpy import ones, sqrt, pi, cos, exp, linspace, zeros
from scipy.special import erf

N = 10
h = 1/N

x = linspace(0, 1, N+1)

w = 4 * ones(N+1)
w[::2] = 2
w[0] = w[-1] = 1

f = exp(x) * sqrt(1 - x)
simpf = h/3 * (w @ f.T)
print(f"simpf = {simpf}")

tsol = sqrt(pi) * erf(1) * exp(1) / 2
print(f"errsimp = {abs(tsol - simpf)}")

N = 10
h = 1/N
x = linspace(0, 1, N+1)
y = linspace(0, 1, N+1)

F = zeros((N+1, N+1))
for i in range(N+1):
    for j in range(N+1):
        F[i, j] = cos(2*x[i] + y[j]) * sqrt(x[i] * y[j])

simpF = h**2/9 * w @ F @ w.T
print(f"simp2dF = {simpF}")

