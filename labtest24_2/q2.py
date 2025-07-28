from numpy import zeros, exp
from scipy.optimize import fsolve


x0 = 5/2

def g(x):
    return (x-1) ** 4 + exp(x) - 3

def dg(x):
    return 4 * (x-1) ** 3 + exp(x)

xs = zeros(4)
xs[0] = x0

for i in range(1, 4):
    xs[i] = xs[i - 1] - g(xs[i-1])/ dg(xs[i-1])

x1 = 0
x2 = x0

while abs(x1 - x2) >= 10 ** (-8):
    xnew = x2 - g(x2) / dg(x2)
    x1 = x2
    x2 = xnew

xe = x2
f1f2 = x2
print(f"x2 = {x2}")

