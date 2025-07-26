from numpy import inf, array
from scipy.linalg import norm

X = array([-9, 5, 1, -4, 12, -7])

print(norm(X, 1))
print(norm(X, 2))
print(norm(X, inf))
