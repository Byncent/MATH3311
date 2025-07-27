from numpy import zeros, exp 
from scipy.optimize import fsolve 

x0 = 3

def f(x):
    return (x-1)**4 + exp(x) - 2

def df(x):
    return 4 * (x-1) ** 3 + exp(x)

xs = zeros(4)
xs[0] = x0

for i in range(1, 4):
    xs[i] = xs[i-1] - f(xs[i-1])/df(xs[i-1])

print(f"x1 = {xs[1]}")
print(f"x2 = {xs[2]}")
print(f"x3 = {xs[3]}")


x1 = 0
x2 = x0

while abs(x1 - x2) >= 10**(-8):
    xn = x2 - f(x2)/df(x2)
    x1 = x2
    x2 = xn

print(f"xe = {x2}")

print(f"invf2 = {fsolve(f, x0)}")