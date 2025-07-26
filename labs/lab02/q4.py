from numpy import inf, identity, linalg
from scipy.linalg import hilbert

I = 5*identity(5)
print(linalg.cond(I, 1))
print(linalg.cond(I, 2))
print(linalg.cond(I, inf))

# i. cond = 1

H = hilbert(5)
print(linalg.cond(H, 1))
print(linalg.cond(H, 2))
print(linalg.cond(H, inf))

H = hilbert(10)
print(linalg.cond(H, 1))
print(linalg.cond(H, 2))
print(linalg.cond(H, inf))

H = hilbert(15)
print(linalg.cond(H, 1))
print(linalg.cond(H, 2))
print(linalg.cond(H, inf))