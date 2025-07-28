from numpy import pi, sin, exp, zeros, diag, array
from numpy.linalg import cond, det, solve
from scipy.linalg import norm, qr

n = 11

A = zeros((n+1, n+1))
for i in range(n+1):
    for j in range(n+1):
        if j == 0:
            A[i][j] = 1
        elif i == 0:
            A[i][j] = 0
        else:
            A[i][j] = 1/(2 * i + 1) ** (j)

print(f"sumA = {A.sum()}")

condA = cond(A, 2)

print(f"condA = {condA}")

comment1 = 'yes'

detA = det(A)

print(f"detA = {detA}")

comment2 = 'no'

Q, R = qr(A)

print(f"diag5Q = {diag(Q)[:5]}")


x = array([0, 1/3, 1/5, 1/7, 1/9])
V = A[:5, :5]
f = lambda x: sin(10 * pi * x) / (100 * exp(x))
print(solve(V, f(x)))
