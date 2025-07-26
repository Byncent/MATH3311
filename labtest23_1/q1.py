from numpy import array, zeros, ones, identity
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu, qr

n = 10
A = zeros((n, n))
for i in range(n):
    for j in range(1, n):
        A[i, j] = (i+j+1)/(i+j+2)
        A[j, i] = (i+j+1)/(i+j+2)
        A[i, i] = i
print(A)

a = A[3][7]
b = A[4][4]
c = A[6][2]

Acheck = norm(A.T@A - identity(n), 2)
print(Acheck)
comment1 = "no"

condA = cond(A, 2)
EigA = eigvals(A)
EigA = sorted(EigA)
comment2 = "no"

PM, L, U = lu(A[0:4,0:4])
PM = PM.T