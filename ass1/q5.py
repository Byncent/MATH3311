from math import exp

x1 = 1
x2 = 1 + 10**(-10)
mu = (x1+x2)/2
sigma2_1 = 1/2 * (x1**2 + x2**2) - mu**2
sigma2_2 = 1/2*((x1-mu)**2 + (x2-mu)**2)

print(sigma2_1)
print(sigma2_2)