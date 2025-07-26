import numpy as np
from numpy.random import randn, seed

n = 10**6
seed(1)
u = randn(n,1)
v = randn(n,1)
b = randn(n,1)

def D_inv_b(b):
    x = np.empty_like(b)
    x[0] = b[0]
    x[1:] = b[1:] - b[:-1]
    return x

Dinv_b = D_inv_b(b)
binv5 = Dinv_b[:5]

# Output
print("binv5:", binv5)