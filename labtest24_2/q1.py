from numpy import pi, cos, zeros, ones, vander, array
from numpy.linalg import cond, det, solve
from scipy.linalg import norm, svd

n = 13
A = zeros((n, n))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            A[i][j] = 1
        else:
            A[i, j] = 1/((2 * i) ** (j))


print(f"sumA = {sum(sum(A))}")

print(f"condA = {cond(A, 2)}")

comment1 = 'no'

print(f"detA = {det(A)}")

comment2 = 'no'

_, s, _ = svd(A)

SumsvA = sum(s)
print(f"SumsvA = {SumsvA}")

x = array([1, 1/2, 1/4, 1/6, 1/8, 1/10])

V = A[:6, :6]

def f(x):
    return (x+1) * cos(2 * pi * x)

veca = solve(V, f(x))
print(f"veca = {veca}")
