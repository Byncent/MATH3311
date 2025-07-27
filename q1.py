from numpy import pi, sin, exp, zeros, ones, sum, diag, array, vander
from numpy.linalg import cond, det, solve
from scipy.linalg import norm, qr

n = 11
A = zeros((n+1, n+1))

for i in range(n+1):
    for j in range(n+1):
        if i == 0 and j != 0:
            A[i][j] = 0
        else:
            A[i][j] = 1/(2*i + 1) ** j
print(f"sumA = {sum(A)}")

print(f"condA = {cond(A, 2)}")

print(f"comment1 = yes")

print(f"detA = {det(A)}")

print(f"comment2 = no")

Q, R = qr(A)

print(f"diag5Q = {diag(Q)[:5]}")

x = array([0, 1/9, 1/7, 1/5, 1/3])

def f(x):
    return sin(10 * pi * x)/(100 * exp(x))

A = vander(x, N=5, increasing=True)

veca = solve(A, f(x))
print(f"veca = {veca}")