from numpy import array, zeros, ones, identity, diag
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu, qr

n = 10

A = zeros((n, n))
for i in range(n):
    for j in range(i, n):
        A[i, j] = (i + j + 1)/(i + j + 2)
        A[j, i] = (i + j + 1)/(i + j + 2)
        A[i, i] = i+1

Acheck = norm(A.T @ A - identity(n))
print(Acheck)

comment1 = "no"

condA = cond(A, 2)
print(condA)

EigA = sorted(eigvals(A))
print(EigA)

commen2 = "yes"
Q, R = qr(A)
Rd = diag(R)[:5]
