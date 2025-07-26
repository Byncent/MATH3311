from numpy import inf, array
from scipy.linalg import norm, eigvals

A = array([
    [3, -2, 0, 5],
    [1, 8, 7, 0],
    [-9, 5, 1, 2],
    [3, -2, 0, 5],
    [3, -4, 0, 5]
])

print(norm(A, 1))
print(norm(A, inf))
print(norm(A, 2))

B = A[0:4,0:4]
print(norm(B, 1))
print(norm(B, inf))
print(norm(B, 2))

print(eigvals(B))