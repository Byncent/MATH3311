import numpy as np


x = 0
while (2 ** (-x) > 0):
    x += 1
print(x)

print(np.finfo(float).tiny)
print(2**(-1073))
print(2**(-1074))
print(2**(-1075))