from numpy import array, zeros, ones, identity, exp
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu

x0 = 3

def g(x):
    return (x+1)**4 + exp(x) - 2

def dg(x):
    return 4*(x+1)**3 + exp(x)

xs = zeros(4)
xs[0] = x0
for i in range(1, 4):
    xs[i] = xs[i-1] - g(xs[i-1])/dg(xs[i-1])

print(xs)

xa = xs[3]
xb = xs[2]
while(abs(xa - xb) > 10**(-15)):
    xnew = xb - g(xb)/dg(xb)
    xa = xb
    xb = xnew

xe = xb
invf2 = xb
print(xb)